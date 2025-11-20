"""
Exercise 1.3: Custom Output (Raw vs Summary) (Stub)
- Fetch Pokémon data from the PokéAPI.
- Display either the full raw JSON or a summarised version based on a parameter.
"""

import httpx, json, pprint

def fetch_pokemon_custom(name, display_raw=False):
    """Fetch Pokémon details and display either raw JSON or a summary."""
   # TODO: Construct the URL using the Pokémon name
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"

    # TODO: Make a GET request to the URL
    data = httpx.get(url)
    
      
    # TODO: Check if the response is successful (status_code == 200)
    if data.status_code == 200:
        mars = data.json()
        types = json.dumps(mars)
        if display_raw:
            pprint.pprint(mars, indent=8) 
        else:
            print("___________________________")
            
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
            print("___________________________")
    else:
        print("Invalid pokemon.")

        
    
    
        

fetch_pokemon_custom("Goodra", False)
fetch_pokemon_custom("Charmy")

# Example usage
# fetch_pokemon_custom("squirtle")  # Display summary by default
# fetch_pokemon_custom("squirtle", display_raw=True)  # Display raw JSON

"""
Hints:
- Use json.dumps(data, indent=4) for raw JSON output.
- Extract specific keys like 'types', 'stats', and 'sprites' for summaries.
- Use if display_raw to toggle between outputs.
"""
