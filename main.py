from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash

from settings import app
from flask import render_template
from forms import RegisterForm, LoginForm
from models import User
from settings import db
from authentication.register import register_user


# ---> Index and About
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


# ---> Authentication


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            register_user(form)
            return render_template('index.html')
        except IntegrityError:
            return render_template('login.html')

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


# ----> Profile CRUD


if __name__=='__main__':
    app.run(debug=True)
