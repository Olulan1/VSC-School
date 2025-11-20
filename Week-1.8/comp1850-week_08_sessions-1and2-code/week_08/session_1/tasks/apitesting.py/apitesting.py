import httpx
"""
url = "https://pokeapi.co/api/v2/pokemon-species/buneary"
response = httpx.get(url)

url = "https://jsonplaceholder.typicode.com/posts"
response1 = httpx.get(url)
print(response1)"""

api_url = "https://gamebrain.co/api/console"
api_key = "1290e1a0a0b54696ab6728f4d28db4a4"

response2 = httpx.get(api_url)
print(response2)