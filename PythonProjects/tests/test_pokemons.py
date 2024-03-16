import requests
import pytest


URL = ' https://api.pokemonbattle.me/v2'
HEADERS = {'Content-type': 'application/json','trainer_token':'31aa683baa1dd7d3a696a8909129c3c6'}

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_trainer_name():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : '326'})
    assert response.json()['data'][0]['trainer_name'] == 'Чойсик'
