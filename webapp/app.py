import os
import database 
import functools
from forms import RegistrationForm, LoginForm
from flask import Flask, render_template, url_for, flash, redirect, session, g
from werkzeug.security import check_password_hash 

app = Flask(__name__)

#secret key für auth.py, generiert mit python secrets.token_hex
app.config['SECRET_KEY'] = 'b9e2ee9c9612c20fe2aeec1149e730b9'
app.secret_key = "studynet-secret-key"

app.config.from_mapping(
    DATABASE=os.path.join(app.instance_path, 'studynet.sqlite')
)
app.cli.add_command(database.init_db)
app.teardown_appcontext(database.close_db)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    #erfolgreich Daten eingegeben flash message
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Registrieren', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    session.clear()
    flash('Du wurdest ausgeloggt.', 'info')
    redirect(url_for('login'))
    
@app.route('/anfragen')
def anfrage():
    return render_template('anfragen.html')

@app.route('/chat')
def nachrichten():
    return render_template('chat.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

# Statische Seiten im Footer / Nav
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/impressum')
def impressum():
    return render_template('impressum.html')

@app.route('/datenschutz')
def datenschutz():
    return render_template('datenschutz.html')

@app.route('/community-richtlinien')
def community_richtlinien():
    return render_template('community-richtlinien.html')


