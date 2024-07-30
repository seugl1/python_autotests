import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2b6230afb87e172579962cb481181791'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN }

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_my_id():
    response_id = requests.get(url = f'{URL}/trainers')
    assert response_id.json()["data"][0]["id"] == '6735'



