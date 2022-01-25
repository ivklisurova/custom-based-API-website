from functools import wraps

from flask_login import current_user
from flask import abort


def login_required(function):
    """Make this page only accessible if authenticated."""

    @wraps(function)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return abort(401)
        else:
            return function(*args, **kwargs)

    return decorated_function
