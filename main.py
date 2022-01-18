from werkzeug.security import generate_password_hash

from settings import app
from flask import render_template
from forms import RegisterForm, LoginForm
from models import User
from settings import db


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
        user = User(
            email=form.email.data,
            name=form.name.data,
            password=generate_password_hash(
                password=form.password.data,
                method='pbkdf2:sha256',
                salt_length=3
            ),
        )
        db.session.add(user)
        db.session.commit()
        return render_template('index.html')

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


# ----> Profile CRUD


if __name__=='__main__':
    app.run(debug=True)
