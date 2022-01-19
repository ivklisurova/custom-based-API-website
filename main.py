from flask import render_template, redirect, url_for, flash
from forms import RegisterForm, LoginForm
from models import User
from settings import app, login_manager
from authentication.register import register_user
from flask_login import login_user, logout_user, current_user
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash
from authentication.login import get_user


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
            return redirect(url_for('index'))
        except IntegrityError:
            flash('You have already signed up wit that email, log in instead', 'error')
            return redirect(url_for('register'))

    return render_template('authentication/register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user(form)
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('index'))
            flash('Password incorrect please try again', 'error')
            return redirect(url_for('login'))
        else:
            flash('That email does not exist, please try again or register', 'error')
            return redirect(url_for('login'))

    return render_template('authentication/login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


# ----> Profile

@app.route('/profile')
def profile():
    return render_template('profile/profile.html')


@app.route('/diary')
def diary():
    return render_template('profile/diary.html')


if __name__=='__main__':
    app.run(debug=True)
