import httpx

url = "https://pokeapi.co/api/v2/pokemon-species/buneary"
response = httpx.get(url)

url = "https://jsonplaceholder.typicode.com/posts"
response1 = httpx