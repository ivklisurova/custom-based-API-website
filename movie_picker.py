import json

from PyMovieDb import IMDB
import random

# Creating an instance of the Cinemagoer class
ia = IMDB()

# Finding the top 250 movies
top = ia.popular_movies(genre=None, start_id=1, sort_by=None)
data = json.loads(top)

random_list = []

for i in range(3):
    movie = random.choice(data['results'])
    random_list.append(movie['name'])
