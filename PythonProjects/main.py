import requests

URL = ' https://api.pokemonbattle.me/v2'
HEADERS = {'Content-type': 'application/json','trainer_token':'31aa683baa1dd7d3a696a8909129c3c6'}

body_1 = {
    "name": "generate",
    "photo": "generate"
}

response_create_pokemon = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body_1)
print(response_create_pokemon.text)

body_2 = {
    
    "pokemon_id": "14153",
    "name": "Бульбик"

}
response_change_name = requests.patch(url = f'{URL}/pokemons', headers = HEADERS, json = body_2)

print(response_change_name.text)

body_3 = {
    "pokemon_id": "14153"
}

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body_3)
print(response_pokeball.text)