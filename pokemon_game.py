import requests

import json

import random

def get_pokemon_data(pokemon_name):

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

    response = requests.get(url)

    if response.status_code == 200:

        pokemon_data = json.loads(response.content)

        return pokemon_data

    else:

        return None

    def get_location_data(location_name):

        url = f"https://pokeapi.co/api/v2/location/{location_name}"

        response = requests.get(url)

        if response.status_code == 200:

            location_data = json.loads(response.content)

            return location_data

        else:

            return None

        def generate_wild_pokemon(location_name):

            location_data = get_location_data(location_name)

            if location_data is not None:

                pokemon_list = []

                for area in location_data['areas']:

                    area_data = get_location_data(area['name'])

                    for encounter in area_data['encounter_method_rates']:

                        if encounter['encounter_method']['name'] == 'walk':

                            for pokemon in encounter['version_details'][0]['encounter_details']:

                                pokemon_data = get_pokemon_data(pokemon['pokemon']['name'])

                                if pokemon_data is not None:
                                    pokemon_list.append(pokemon_data)

                if len(pokemon_list) > 0:

                    return random.choice(pokemon_list)

                else:

                    return None

            else:

                return None

            def display_pokemon_stats(pokemon_data):

                if pokemon_data is not None:

                    print(f"Name: {pokemon_data['name'].capitalize()}")

                    print(f"Type: {pokemon_data['types'][0]['type']['name'].capitalize()}")

                    print("Moves:")

                    for move in pokemon_data['moves']:
                        print(f"- {move['move']['name'].capitalize()}")

                    print("Stats:")

                    for stat in pokemon_data['stats']:
                        print(f"- {stat['stat']['name'].capitalize()}: {stat['base_stat']}")

                else:

                    print("Pokemon not found.")

                    def start_game():

                        print("Welcome to the Pokemon text-based game!")

                        print("Choose your starting location:")

                        print("1. Pallet Town")

                        print("2. Viridian City")

                        choice = input("> ")

                        if choice == "1":

                            location_name = "pallet-town"

                        elif choice == "2":

                            location_name = "viridian-city"

                        else:

                            print("Invalid choice.")

                            return

                        wild_pokemon = generate_wild_pokemon(location_name)

                        display_pokemon_stats(wild_pokemon)