# Kristian Wareing
# 07/12/2026
# CSD-325 Module 7 Assignment
# Purpose: Unit test for the city_country() function in city_functions.py.

import unittest
from city_functions import city_country


class CitiesTestCase(unittest.TestCase):
    """Tests for city_functions.py."""

    def test_city_country(self):
        """Do city and country values return 'City, Country'?"""
        formatted_city = city_country("Santiago", "Chile")
        self.assertEqual(formatted_city, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()
