import requests

def get_pokemon(url):
    res = requests.get(url).json()
    return("Pokemon Name: " + res.get('name'))

print('Example 1')
print(get_pokemon("http://pokeapi.co/api/v2/pokemon/1/"))