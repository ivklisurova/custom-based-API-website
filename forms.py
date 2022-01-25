from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FloatField, TextAreaField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired, URL


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class UpdateUserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Update Profile Info')


class AddMovieForm(FlaskForm):
    add_movie_title = StringField('Search Movie', validators=[DataRequired(message='This field is required')])
    submit = SubmitField('Add')


class EditMovieForm(FlaskForm):
    update_rating = FloatField('Your rating out of 10, e.g 7.5',
        validators=[DataRequired(message='This field is required')])
    update_review = TextAreaField('Your review', validators=[DataRequired(message='This field is required')])
    submit = SubmitField('Submit')
