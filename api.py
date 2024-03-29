import requests
from settings import OMDBb_API_KEY, OMDb_LINK
from settings import db
from models import Movie
from flask import flash


def add_movie(movie_name, user_id):
    params = {
        'apikey': [OMDBb_API_KEY],
        't': f'{movie_name}'

    }

    response = requests.get(url=OMDb_LINK, params=params)
    response.raise_for_status()
    data = response.json()
    try:
        new_movie = Movie(title=movie_name, year=data['Year'], description=data['Plot'],
            ranking=float(data['Ratings'][0]['Value'].split('/')[0]), img_url=data['Poster'], user_id=user_id)
        db.session.add(new_movie)
        db.session.commit()
    except KeyError:
        flash('Movie not found', 'error')


def get_movie(movie_name):
    params = {
        'apikey': [OMDBb_API_KEY],
        't': f'{movie_name}'

    }
    response = requests.get(url=OMDb_LINK, params=params)
    response.raise_for_status()
    data = response.json()
    return data
