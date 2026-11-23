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


def get_own_post(post_id)
    """Lädt einen Beitrag. 404 = gibt es nicht, 403 = gehört jemand anderem."""
    post = get_db().execute('SELECT * FROM post WHERE id = ?', (post_id,)).fetchone()
    if post is None:
        abort(404)
    if post['author_id'] != g.user['id']
        abort(403)
    return post
