"""
CSD-325 Module 9 - API Tutorial Program
Kristian Wareing

Part 1: test the connection (status code)
Part 2: retrieve the current astronauts in space and format the output
"""

import requests


def test_connection():
    """Simple connection test - just print the status code."""
    print("--- Connection Test ---")

    response = requests.get("http://www.google.com")
    print("google.com status code:", response.status_code)

    response = requests.get("http://api.open-notify.org/astros.json")
    print("open-notify status code:", response.status_code)
    print()


def get_astronauts():
    """Retrieve current astronauts and format the output."""
    print("--- People Currently in Space ---")

    response = requests.get("http://api.open-notify.org/astros.json")

    if response.status_code != 200:
        print("Request failed with status code:", response.status_code)
        return

    data = response.json()

    # unformatted response
    print("\nRaw response:")
    print(data)

    # formatted response
    print("\nFormatted response:")
    print("Number of people in space:", data["number"])
    print()

    for person in data["people"]:
        print("Name: " + person["name"])
        print("Craft: " + person["craft"])
        print()


def main():
    test_connection()
    get_astronauts()


if __name__ == "__main__":
    main()