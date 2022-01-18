from models import User


def get_user(user_form):
    email = user_form.email.data
    user = User.query.filter_by(email=email).first()
    return user
