import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2b6230afb87e172579962cb481181791'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN }
BODY = {
    "name": "generate",
    "photo_id": -1
}

BODY_NEW_NAME = {
    "pokemon_id": "45826",
    "name": "Granata10",
    "photo_id": 2
}

BODY_GETPKBL = {
    "pokemon_id": "45825"
}


response = requests.post(url= f'{URL}/pokemons', headers = HEADER, json = BODY)
print(response.text)

response_namechange = requests.put(url= f'{URL}/pokemons', headers = HEADER, json = BODY_NEW_NAME)
print(response_namechange.text)

response_getinpkbl = requests.post(url= f'{URL}/trainers/add_pokeball', headers = HEADER, json = BODY_GETPKBL)
print(response_getinpkbl.text)