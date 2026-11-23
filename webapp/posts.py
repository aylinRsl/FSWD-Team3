"""
Eingeloggte Bewohner*innen können eigene Beiträge erstellen, anzeigen,
bearbeiten, auf "erledigt" setzen und löschen.
"""
import functools
from flask import (Blueprint, abort, flash, g, redirect, render_template,
                   request, session, url_for)

from database import get_db
from forms import ConfirmForm, PostForm

# Alle URLs dieses Blueprints beginnen mit /beitraege
bp = Blueprint('posts', __name__, url_prefix='/beitraege')

# TODO (Absprache mit Nasty) löschen, sobald auth.py g.user selbst lädt
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

 
def login_required(view):
    """Decorator: leitet nicht eingeloggte Personen zum Login um."""
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.get('user') is None:
            flash('Bitte logge dich zuerst ein.', 'warning')
            return redirect(url_for('login'))
        return view(**kwargs)
    return wrapped_view       

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


