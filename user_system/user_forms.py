from wtforms.fields import simple, core
from wtforms import Form, validators, widgets, ValidationError
import calendar


class LoginForm(Form):
    username = simple.StringField(
        label='Username',
        widget=widgets.TextInput(),
        validators=[validators.DataRequired(message="Username can not be empty")])
    password = simple.PasswordField(
        label='Password',
        widget=widgets.PasswordInput(),
        validators=[validators.DataRequired(message='Password can not be empty')])
    submit = simple.SubmitField(
        label='Submit',
        widget=widgets.SubmitInput()
    )


class RegistrationForm(Form):
    username = simple.StringField(
        label='Username',
        widget=widgets.TextInput(),
        validators=[validators.DataRequired(message="Username can not be empty"),
                    validators.Length(6,40,'Need to be more than 6 characters')])
    password = simple.PasswordField(
        label='Password',
        widget=widgets.PasswordInput(),
        validators=[validators.DataRequired(message='Password can not be empty'),
                    validators.Length(6,40,'Need to be more than 6 characters')])
    password2 = simple.PasswordField(
        label='Repeat Password',
        widget=widgets.PasswordInput(),
        validators=[validators.DataRequired(message='Password can not be empty'),
                    validators.EqualTo('password',message='Two password not same')])
    email = simple.StringField(
        label='Email',
        widget=widgets.TextInput(),
        validators=[validators.DataRequired(message='Email can not be empty'),
                    validators.Email(message='Wrong Email Syntax')])
    submit = simple.SubmitField(
        label='Submit',
        widget=widgets.SubmitInput())


