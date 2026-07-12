# Kristian Wareing
# 07/12/2026
# CSD-325 Module 7 Assignment
# Purpose: Build a formatted city string with optional population and language.


def city_country(city, country, population="", language=""):
    """Return 'City, Country' plus population and language when provided."""
    formatted_city = f"{city.title()}, {country.title()}"

    # Only append the population when the caller supplies one.
    if population:
        formatted_city += f" - population {population}"

    # Only append the language when the caller supplies one.
    if language:
        formatted_city += f", {language.title()}"

    return formatted_city


# Call the function with two, three, and four arguments.
print(city_country("santiago", "chile"))
print(city_country("tokyo", "japan", 13960000))
print(city_country("oakland", "united states", 440000, "english"))
