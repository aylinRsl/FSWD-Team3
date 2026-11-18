from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import InputRequired, Length, Email, EqualTo, Regexp


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[InputRequired(), Length(min=3, max=20)])
    email = StringField('HWR-E-Mail',
                        validators=[InputRequired(), Email(),
                                    Regexp(r'^[^@\s]+@stud\.hwr-berlin\.de$',
                                           message='Bitte deine HWR-Studierenden-Adresse (@stud.hwr-berlin.de) verwenden.')])
    # TODO: Wohnheime in Dorm Tabelle hinterlegen, SelectField mit Wohnheimen befüllen
    # https://www.reddit.com/r/flask/comments/semnrv/populating_select_field_in_forms/
    dormitory = SelectField('Wohnheim', coerce=int,
                            validators=[InputRequired()])
    password = PasswordField('Password',
                             validators=[InputRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Registrieren')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[InputRequired(), Email()])
    password = PasswordField('Password',
                             validators=[InputRequired()])
    # TODO überprüfen
    # remember = BooleanField('Anmeldung speichern')
    submit = SubmitField('Einloggen')