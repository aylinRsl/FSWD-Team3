from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, RadioField, TextAreaField
from wtforms.validators import InputRequired, DataRequired, Length, Email, EqualTo, Regexp, ValidationError, Optional

#@aylinRsl
# Email DOmains der verschiedenen berliner Hochschulen: Konstante für den Validator
ALLOWED_DOMAINS = [
    'stud.hwr-berlin.de',
    'hwr-berlin.de',
    'zedat.fu-berlin.de',      # FU
    'fu-berlin.de',            # FU 
    'student.hu-berlin.de',    # HU
    'htw-berlin.de',           # HTW
    'student.htw-berlin.de',   # HTW 
    'bht-berlin.de',           # BHT
    ]

# Validator mit 2 Parametern die WTForms akzeptiert
def uni_email(form, field):
    #Domain splitten bei @. rsplit: von Rechts, -1: nimmt letztes Element (Domain)
    domain = field.data.rsplit('@', 1) [-1].lower()
    if domain not in ALLOWED_DOMAINS:
        raise ValidationError('Bitte deine Uni-Email verwenden!')

# erbt von FlaskForm, prüft die Registrierung
class RegistrationForm(FlaskForm):
    username = StringField('Username',
                        validators=[InputRequired(), Length(min=3, max=20)])
    
    #Filter nötig da sonst Leerzeichen oder chars aus copy paste die email validierung verhindern
    email = StringField('Uni E-Mail',
                        filters=[lambda x: x.strip() if x is not None else x],
                        validators=[InputRequired(), Email(), uni_email])
    
    dormitory = SelectField('Wohnheim', coerce=int,
                        validators=[InputRequired()])
    
    verification_code = StringField('Wohnheim Code', 
                        validators=[InputRequired()] )
    
    password = PasswordField('Password',
                        validators=[InputRequired(), Length(min=8)])
    
    confirm_password = PasswordField('Confirm Password',
                        validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Registrieren')

class LoginForm(FlaskForm):
    # filter aus dem selben Grund wie bei registerForm
    email = StringField('Uni-E-Mail',
                        filters=[lambda x: x.strip() if x is not None else x],
                        validators=[InputRequired(), Email()])
    
    password = PasswordField('Password',
                        validators=[InputRequired()])
    # TODO überprüfen
    # remember = BooleanField('Anmeldung speichern')
    submit = SubmitField('Einloggen')

# Formulare für das Feature "CRUD für Beiträge" (Narin)

class PostForm(FlaskForm):
    # "Ich suche ..." / "Ich biete an ..."
    type = RadioField('Was möchtest du?',
                      choices=[('request', 'Ich suche …'),
                               ('offer', 'Ich biete an …')],
                      validators=[InputRequired(message='Bitte wähle suchen oder anbieten.')])

    title = StringField('Titel',
                        validators=[DataRequired(message='Bitte gib einen Titel ein.'),
                                    Length(max=100)])

    description = TextAreaField('Beschreibung',
                                validators=[Optional(), Length(max=2000)])

    # Die Auswahl (choices) wird in posts.py aus der Tabelle category geladen
    category_id = SelectField('Kategorie', coerce=int,
                              validators=[InputRequired()])

    reward_type = SelectField('Gegenleistung',
                              choices=[('none', 'Keine'),
                                       ('thanks', 'Ein Dankeschön (z. B. Essen)'),
                                       ('money', 'Kleiner Geldbetrag')],
                              default='none')

    # bewusst kein Optional(): sonst würde validate_reward_note nicht laufen
    reward_note = StringField('Details zur Gegenleistung (optional)',
                              validators=[Length(max=200)])

    submit = SubmitField('Anfrage veröffentlichen')

    # Eigener Validator: WTForms ruft validate_<feldname> automatisch auf
    def validate_reward_note(self, field):
        if self.reward_type.data == 'money' and not field.data:
            raise ValidationError('Bitte gib bei Geld kurz an, wie viel du anbietest.')

class ConfirmForm(FlaskForm):
    """Leeres Formular nur für das CSRF-Token (Löschen, Status ändern)."""
    submit = SubmitField('Bestätigen')

class ContactForm(FlaskForm):
    email = StringField('E-Mail', validators=[DataRequired(), Email()])
    subject = StringField('Betreff', validators=[DataRequired()])
    message = TextAreaField('Dein Anliegen', validators=[DataRequired()])
    submit = SubmitField('Absenden')