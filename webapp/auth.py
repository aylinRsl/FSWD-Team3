# login_required und load_logged_in_user werden hierhin ausgelagert
# posts.py kann login_requried nicht aus app.py importieren, da in app.py schon posts importiert wird
import functools
from flask import g, session, flash, redirect, url_for
import database

# vor Requests sollen eingeloggte User aus Session geladen werden
@app.before_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = database.get_db().execute(
            'SELECT id, username, email, dormitory_id FROM user WHERE id = ?;',
            [user_id]
        ).fetchone()
        
# neuer decorator, sodass nur eingeloggte User die Route verwenden können
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            flash('Bitte zuerst einloggen.', 'warning')
            return redirect(url_for('login'))
        return view(**kwargs)
    return wrapped_view