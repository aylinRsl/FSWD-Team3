from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import InputRequired, Length, Email, EqualTo, Regexp, ValidationError

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