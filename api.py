import requests

OMDBb_API_KEY = '8d593346'
OMDb_LINK = 'http://www.omdbapi.com/'

params = {
    'apikey': [OMDBb_API_KEY],
    't': 'The Godfather',

}

response = requests.get(url=OMDb_LINK, params=params)
response.raise_for_status()
data = response.json()
print(data)