from imdb import IMDb
import random


ia = IMDb()

top = ia.get_top250_movies()

random_list = []

for i in range(3):
    movie = random.choice(top)
    random_list.append(movie['title'])
