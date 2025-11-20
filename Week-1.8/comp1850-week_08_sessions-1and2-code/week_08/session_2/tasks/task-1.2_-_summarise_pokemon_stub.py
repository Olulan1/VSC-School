"""
Exercise 1.2: Summarise Pokémon Details (Stub)
- Fetch Pokémon data from the PokéAPI.
- Extract specific details: name, types, stats, and image URL.
- Display the extracted details in a readable format.
""" # gimme postman.co

import httpx, json, pprint

def summarise_pokemon(name):
    """Fetch and summarise Pokémon details."""
    # TODO: Construct the URL using the Pokémon name
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"

    # TODO: Make a GET request to the URL
    data = httpx.get(url)

    # TODO: Check if the response is successful (status_code == 200)
    if data.status_code == 200:
        print("___________________________")
        mars = data.json()
        types = json.dumps(mars)
        types = [t['type']['name'] for t in mars['types']]
        print(f"Name: {mars['name'].upper()}")
        print("Types: ", end="")
        
        for i in range (0, len(types)):
            print(types[i],",", end="")
        print()
        print("Base Stats: ")
        for i in range (0, len(mars['stats'])):
            print(mars['stats'][i]['stat']['name'].upper(),": ", end="")
            print(mars['stats'][i]['base_stat'])
        print()
        print("Image URL: ",mars['sprites']['front_default'])

        
    # Name/Types/BaseStats/ImageURL
        
    
    else:
        # TODO: Print an error message if the Pokémon is not found
        print("Pokemon not found.")


summarise_pokemon("goodra")

    # TODO: Parse the JSON response
    

    # TODO: Extract the Pokémon's name
    

    # TODO: Extract the Pokémon's types
    

    # TODO: Extract the Pokémon's base stats
    

    # TODO: Extract the Pokémon's image URL
    

    # TODO: Print the details in a readable format
#     print(f"Name: {name}")
#     print(f"Types: {', '.join(types)}")
#     print("Base Stats:")
#     for stat, value in stats.items():
#         print(f"  {stat.capitalize()}: {value}")
#     print(f"Image URL: {image_url}")
# else:
#     # TODO: Print an error message if the Pokémon is not found
#     print(f"Error: Pokémon '{name}' not found!")

# Example usage
# summarise_pokemon("squirtle")

"""
Hints:
- Use data['types'] for the Pokémon’s types.
- Use data['stats'] for the Pokémon’s base stats.
- Use a loop to format and display lists or dictionaries.
"""
