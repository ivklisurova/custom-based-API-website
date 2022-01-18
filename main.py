from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash

from settings import app, login_manager
from flask import render_template, redirect, url_for
from forms import RegisterForm, LoginForm
from models import User
from authentication.register import register_user
from flask_login import login_user


# ---> Index and About
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


# ---> Authentication

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('index'))
            return redirect(url_for('login'))
        else:
            return redirect(url_for('register'))

    return render_template('login.html', form=form)



# ----> Profile CRUD


if __name__=='__main__':
    app.run(debug=True)
