from flask import render_template, redirect, url_for, flash
from forms import RegisterForm, LoginForm, AddMovieForm, UpdateUserForm
from models import User, Movie
from settings import app, login_manager, db
from authentication.register import register_user
from flask_login import login_user, logout_user, current_user
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash
from authentication.login import get_user
from api import add_movie


# ---> Index
@app.route('/')
def index():
    return render_template('index.html')


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

@app.route('/profile<int:userid>', methods=['GET', 'POST'])
def profile(userid):
    user_profile = User.query.get(userid)
    edit_profile_form = UpdateUserForm(
        email=current_user.email,
        name=current_user.name,
    )
    if edit_profile_form.validate_on_submit():
        user_profile.email = edit_profile_form.email.data
        user_profile.name = edit_profile_form.name.data
        db.session.commit()
        return redirect(url_for('profile', userid=userid))
    return render_template('profile/profile.html', form=edit_profile_form)


# ----> Diary

@app.route('/diary', methods=['GET', 'POST'])
def diary():
    add_movie_form = AddMovieForm()

    user_movie_list = db.session.query(Movie).filter(Movie.user_id==current_user.id).all()
    print(user_movie_list)

    if add_movie_form.validate_on_submit():
        movie = add_movie_form.add_movie_title.data
        add_movie(movie, current_user.id)
        return redirect(url_for('diary'))
    return render_template('profile/diary.html', form=add_movie_form, movie_list=user_movie_list)


# ----> Diary /Update and delete cards/

@app.route('/<int:record_id>')
def delete_movie(record_id):
    record_to_delete = Movie.query.get(record_id)
    db.session.delete(record_to_delete)
    db.session.commit()
    return redirect(url_for('diary'))


if __name__=='__main__':
    app.run(debug=True)
