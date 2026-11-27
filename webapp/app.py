import os
import database 
import functools
import sqlite3
import auth
from auth import login_required
from forms import ContactForm, RegistrationForm, LoginForm
from flask import Flask, render_template, url_for, flash, redirect, session
from flask_mail import Mail, Message
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
#TODO: Mail server und port hier als platzhälter
app.config['MAIL_SERVER'] = 'localhost'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = None
app.config['MAIL_PASSWORD'] = None
app.config['MAIL_DEFAULT_SENDER'] = None

mail = Mail(app)

#TODO: überprüfen, secret key auslagern
app.config['SECRET_KEY'] = 'secret-key'
app.secret_key = "studynet-secret-key"

app.config.from_mapping(
    DATABASE=os.path.join(app.instance_path, 'studynet.sqlite')
)
app.cli.add_command(database.init_db)
app.teardown_appcontext(database.close_db)

# Feature "CRUD für Beiträge" Routen aus posts.py einbinden
import posts
app.register_blueprint(posts.bp)

# user laden -> Funktion steht in auth.py
app.before_request(auth.load_logged_in_user)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    db_con = database.get_db()
    
    dorms = db_con.execute('SELECT id, name FROM dormitory ORDER BY name;').fetchall()
    form.dormitory.choices = [(d['id'], d['name']) for d in dorms]
    
    if form.validate_on_submit():
        dorm = db_con.execute(
            'SELECT verification_code FROM dormitory WHERE id = ?;',
            [form.dormitory.data]
        ).fetchone()
        
        if not check_password_hash(dorm['verification_code'], form.verification_code.data):
            form.verification_code.errors.append('Falscher Wohnheim-Code.')
        else:
            try:
                db_con.execute(
                    'INSERT INTO user (username, email, password_hash, is_verified, dormitory_id) '
                    'VALUES (?, ?, ?, 1, ?);',
                    [form.username.data, form.email.data.lower(),
                    generate_password_hash(form.password.data), form.dormitory.data]
                )
                db_con.commit()
                flash('Registrierung erfolgreich. Bitte einloggen.', 'success')
                return redirect(url_for('login'))
            except sqlite3.IntegrityError:
                flash('Username oder Email ist bereits vergeben', 'warning')
                
    return render_template('register.html', title='Registrieren', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = database.get_db().execute(
            'SELECT id, password_hash FROM user WHERE email = ?;',
            [form.email.data.lower()]
        ).fetchone()
        if user is None or not check_password_hash(user['password_hash'], form.password.data):
            flash('E-Mail oder Passwort ist falsch.', 'danger')
        else:
            session.clear()
            session['user_id'] = user['id']
            flash('Erfolgreich eingeloggt.', 'success')
            return redirect(url_for('home'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.clear()
    flash('Du wurdest ausgeloggt.', 'info')
    return redirect(url_for('login'))
    
@app.route('/anfragen')
#@login_required
def anfrage():
    return render_template('anfragen.html')

@app.route('/chat')
#@login_required
def nachrichten():
    return render_template('chat.html')

@app.route('/profile')
#@login_required
def profile():
    return render_template('profile.html')

# Statische Seiten im Footer / Nav
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/kontaktformular', methods=['GET', 'POST'])
def kontaktformular():
    form = ContactForm()
    if form.validate_on_submit():
        email = form.email.data
        subject = form.subject.data
        message = form.message.data

        # E-Mail an den Administrator senden
        #TODO: E-Mail-Adresse des Administrators anpassen, zur Überlegung ob E-Mail der Admins direkt in Code schreiben
        msg = Message(subject=subject, 
                      recipients=['admin@example.com'],
                      body=f""""
                        Von: {email}
                        Betreff: {subject}
                        Anliegen: {message}
                      """)
        mail.send(msg)
        flash('Deine Nachricht wurde gesendet!', 'success')
        return redirect(url_for('kontaktformular'))
    return render_template('kontaktformular.html', form=form)

@app.route('/impressum')
def impressum():
    return render_template('impressum.html')

@app.route('/datenschutz')
def datenschutz():
    return render_template('datenschutz.html')

@app.route('/community-richtlinien')
def community_richtlinien():
    return render_template('community-richtlinien.html')
