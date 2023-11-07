from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    name=  StringField('Name', validators=[DataRequired(), Length(min=2)]),
    email=  StringField('Email', validators=[DataRequired(), Email()]),
    phone=  StringField('Phone', validators=[DataRequired(), Length(min=2)]),
    lastname=  StringField('LastName', validators=[DataRequired(), Length(min=2)]),
    password=  PasswordField('Password', validators=[DataRequired(), Length(min=2)]),
    confirm_password=  PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')]),
    submit = SubmitField('Sign Up')
    

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')