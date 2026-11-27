"""
Eingeloggte Bewohner*innen können eigene Beiträge erstellen, anzeigen,
bearbeiten, auf "erledigt" setzen und löschen.
"""
from flask import (Blueprint, abort, flash, g, redirect, render_template,
                   request, url_for)
from auth import login_required
from database import get_db
from forms import ConfirmForm, PostForm

# Alle URLs dieses Blueprints beginnen mit /beitraege
bp = Blueprint('posts', __name__, url_prefix='/beitraege')   

def get_category_choices():
    """Liest alle Kategorien für das Auswahlfeld aus der DB."""
    rows = get_db().execute('SELECT id, name FROM category ORDER BY name').fetchall()
    return [(row['id'], row['name']) for row in rows]


def get_own_post(post_id):
    """Lädt einen Beitrag. 404 = gibt es nicht, 403 = gehört jemand anderem."""
    post = get_db().execute('SELECT * FROM post WHERE id = ?', (post_id,)).fetchone()
    if post is None:
        abort(404)
    if post['author_id'] != g.user['id']:
        abort(403)
    return post

# READ: eigene Beiträge (optional gefiltert: ?typ=request oder ?typ=offer)
@bp.route('/meine')
@login_required
def my_posts():
    post_type = request.args.get('typ')
    sql = ('SELECT p.id, p.title, p.description, p.type, p.status, '
           '       p.reward_type, p.reward_note, p.created_at, '
           '       c.name AS category_name '
           'FROM post p JOIN category c ON p.category_id = c.id '
           'WHERE p.author_id = ?')
    params = [g.user['id']]
    if post_type in ('request', 'offer'):
        sql += ' AND p.type = ?'
        params.append(post_type)
    sql += ' ORDER BY p.created_at DESC, p.id DESC'

    posts = get_db().execute(sql, params).fetchall()
    return render_template('posts/my_posts.html', posts=posts,
                           post_type=post_type, csrf_form=ConfirmForm())


# CREATE: neuen Beitrag anlegen
@bp.route('/neu', methods=['GET', 'POST'])
@login_required
def create():
    form = PostForm()
    form.category_id.choices = get_category_choices()

 
    if request.method == 'GET' and request.args.get('typ') in ('request', 'offer'):
        form.type.data = request.args.get('typ')

    if form.validate_on_submit():
        db = get_db()
        db.execute(
            'INSERT INTO post (title, description, type, reward_type, '
            '                  reward_note, author_id, dormitory_id, category_id) '
            'VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
            (form.title.data, form.description.data, form.type.data,
             form.reward_type.data, form.reward_note.data,
             g.user['id'], g.user['dormitory_id'], form.category_id.data)
        )   
        db.commit()
        flash('Dein Beitrag wurde veröffentlicht.', 'success') 
        return redirect(url_for('posts.my_posts'))

    return render_template('posts/form.html', form=form, heading='Anfrage erstellen')



# UPDATE: eigenen Beitrag bearbeiten
@bp.route('/<int:post_id>/bearbeiten', methods=['GET', 'POST'])
@login_required
def edit(post_id):
    post = get_own_post(post_id)
    form = PostForm(data=dict(post))      # GET: mit alten Werten vorausfüllen
    form.category_id.choices = get_category_choices()
    form.submit.label.text = 'Änderungen speichern'

    if form.validate_on_submit():
        db = get_db()
        db.execute(
            'UPDATE post SET title = ?, description = ?, type = ?, reward_type = ?, '
            '                reward_note = ?, category_id = ? '
            'WHERE id = ? AND author_id = ?',
            (form.title.data, form.description.data, form.type.data,
             form.reward_type.data, form.reward_note.data, form.category_id.data,
             post_id, g.user['id'])
        )
        db.commit()
        flash('Dein Beitrag wurde aktualisiert.', 'success')
        return redirect(url_for('posts.my_posts'))

    return render_template('posts/form.html', form=form, post=post, heading='Beitrag bearbeiten')

# UPDATE: Status offen <-> erledigt
@bp.route('/<int:post_id>/status', methods=['POST'])
@login_required
def toggle_status(post_id):

    post = get_own_post(post_id)
    if not ConfirmForm().validate_on_submit():   # prüft das CSRF-Token
        abort(400)

    if post['status'] == 'open':
        new_status = 'done'
    else:
        new_status = 'open'

    db = get_db()
    db.execute('UPDATE post SET status = ? WHERE id = ? AND author_id = ?',
               (new_status, post_id, g.user['id']))
    
    db.commit()
    flash('Status wurde geändert.', 'info')
    return redirect(url_for('posts.my_posts'))

# eigenen Beitrag löschen 
@bp.route('/<int:post_id>/loeschen', methods=['GET', 'POST'])
@login_required
def delete(post_id):
    post = get_own_post(post_id)
    db = get_db()

  
    # Beiträge mit Nachrichten nicht löschen (ON DELETE CASCADE
    # würde sonst alle Chats mitlöschen), stattdessen auf "erledigt" setzen.
    message = db.execute('SELECT id FROM message WHERE post_id = ?',
                         (post_id,)).fetchone()
    if message is not None:


        flash('Zu diesem Beitrag gibt es schon Nachrichten. '
              'Setze ihn bitte auf "erledigt", statt ihn zu löschen.', 'warning')
        return redirect(url_for('posts.my_posts'))

    form = ConfirmForm()
    if form.validate_on_submit():
        db.execute('DELETE FROM post WHERE id = ? AND author_id = ?', (post_id, g.user['id']))
        db.commit()
        flash('Dein Beitrag wurde gelöscht.', 'success')
        return redirect(url_for('posts.my_posts'))

    return render_template('posts/delete.html', post=post, form=form)  
