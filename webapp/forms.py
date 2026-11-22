from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, RadioField, TextAreaField
from wtforms.validators import InputRequired, DataRequired, Length, Email, EqualTo, Regexp, ValidationError, Optional

# Email DOmains der verschiedenen berliner Hochschulen: Konstante für den Validator
ALLOWED_DOMAINS = [
    'stud.hwr-berlin.de'
    'hwr-berlin.de'
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
    
    email = StringField('Uni-E-Mail',
                        validators=[InputRequired(), Email(), uni_email])
    
    # TODO: Wohnheime in Dorm Tabelle hinterlegen, SelectField mit Wohnheimen befüllen
    # https://www.reddit.com/r/flask/comments/semnrv/populating_select_field_in_forms/

    dormitory = SelectField('Wohnheim', coerce=int,
                        validators=[InputRequired()])
    #TODO: Verification Codes
    password = PasswordField('Password',
                        validators=[InputRequired()])
    
    confirm_password = PasswordField('Confirm Password',
                        validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Registrieren')

class LoginForm(FlaskForm):
    email = StringField('Uni-E-Mail',
                        validators=[InputRequired(), Email()])
    
    password = PasswordField('Password',
                        validators=[InputRequired()])
    # TODO überprüfen
    # remember = BooleanField('Anmeldung speichern')
    submit = SubmitField('Einloggen')

# Formulare für das Feature "CRUD für Beiträge" (Narin)
def strip_text(value):
    """Filter: entfernt Leerzeichen am Anfang/Ende ("   " wird zu "")."""
    return value.strip() if isinstance(value, str) else value

class PostForm(FlaskForm):
    # "Ich suche ..." / "Ich biete an ..." 
    type = RadioField('Was möchtest du?',
                      choices=[('request', 'Ich suche …')
                               ('offer', 'Ich biete an …')]
                      validators=[InputRequired(message='Bitte wähle suchen oder anbieten.')])

title = StringField('Titel', filters=[strip_text],
                        validators=[DataRequired(message='Bitte gib einen Titel ein.'),
                                    Length(max=100)])

