from flask_login import login_user
from models import User
from werkzeug.security import generate_password_hash
from settings import db



def register_user(user_form):
    user = User(
        email=user_form.email.data,
        name=user_form.name.data,
        password=generate_password_hash(
            password=user_form.password.data,
            method='pbkdf2:sha256',
            salt_length=3
        ),
    )
    db.session.add(user)
    db.session.commit()
    login_user(user)
