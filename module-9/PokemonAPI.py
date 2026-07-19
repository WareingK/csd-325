"""
CSD-325 Module 9 - API of My Choice
Kristian Wareing

API: PokeAPI (https://pokeapi.co/docs/v2)
No API key or account required.

This program tests the connection, prints the raw unformatted response, and
then prints the same data formatted the same way as the tutorial program.
"""

import requests

BASE_URL = "https://pokeapi.co/api/v2"
POKEMON = ["pikachu", "charizard", "snorlax"]


def test_connection():
    """Test the connection to the API and print the status code."""
    print("--- Connection Test ---")

    response = requests.get(BASE_URL + "/pokemon/pikachu")
    print("PokeAPI status code:", response.status_code)

    if response.status_code == 200:
        print("Connection successful.")
    else:
        print("Connection failed.")

    print()
    return response.status_code == 200


def get_pokemon(name):
    """Request a single Pokemon and return the JSON response."""
    response = requests.get(BASE_URL + "/pokemon/" + name)

    if response.status_code != 200:
        print("Request for " + name + " failed with status code:", response.status_code)
        return None

    return response.json()


def print_raw(data):
    """Print the response with no formatting."""
    print("--- Raw Response (no formatting) ---")
    print(data)
    print()


def print_formatted(data):
    """Print the response formatted, the same way as the tutorial program."""
    print("Name: " + data["name"])
    print("Pokedex Number: " + str(data["id"]))
    print("Height: " + str(data["height"]))
    print("Weight: " + str(data["weight"]))
    print("Base Experience: " + str(data["base_experience"]))

    print("Types:")
    for slot in data["types"]:
        print("   " + slot["type"]["name"])

    print("Abilities:")
    for slot in data["abilities"]:
        if slot["is_hidden"]:
            print("   " + slot["ability"]["name"] + " (hidden)")
        else:
            print("   " + slot["ability"]["name"])

    print()


def main():
    if not test_connection():
        return

    # first request printed raw, with no formatting
    first = get_pokemon(POKEMON[0])

    if first is None:
        return

    print_raw(first)

    # same data plus the rest of the list, formatted
    print("--- Formatted Response ---")
    print_formatted(first)

    for name in POKEMON[1:]:
        data = get_pokemon(name)
        if data is not None:
            print_formatted(data)


if __name__ == "__main__":
    main()
