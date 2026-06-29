"""
Title: sitka_high_low_kw.py
Author: Kristian Wareing
Date: June 2026
Description: A program that reads Sitka, Alaska weather data from a CSV file
             and displays either high or low temperatures for 2018 in a
             matplotlib graph. The user selects highs, lows, or exit from
             a menu that loops until they choose to quit.
"""

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

# -- Constants --
FILENAME = 'sitka_weather_2018_simple.csv'

def load_weather_data():
    """
    Reads the CSV file and returns two lists:
    dates (datetime objects) and a dict with highs and lows lists.
    """
    dates = []
    highs = []
    lows = []

    with open(FILENAME) as f:
        reader = csv.reader(f)
        header_row = next(reader)  # skip header

        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            highs.append(int(row[5]))   # TMAX column
            lows.append(int(row[6]))    # TMIN column

    return dates, highs, lows


def plot_highs(dates, highs):
    """
    Plots the daily high temperatures in red.
    """
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')

    plt.title("Daily High Temperatures - Sitka, AK 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


def plot_lows(dates, lows):
    """
    Plots the daily low temperatures in blue.
    """
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue')

    plt.title("Daily Low Temperatures - Sitka, AK 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


def display_menu():
    """
    Prints the main menu options to the console.
    """
    print("\n========================================")
    print("  Sitka, AK 2018 Weather Data Viewer")
    print("========================================")
    print("  H - View High Temperatures")
    print("  L - View Low Temperatures")
    print("  E - Exit")
    print("========================================")


def main():
    """
    Main function. Loads weather data once, then loops displaying
    the menu until the user chooses to exit.
    """
    # Load data once before the loop
    dates, highs, lows = load_weather_data()

    # Main loop
    while True:
        display_menu()
        choice = input("  Enter your choice: ").strip().upper()

        if choice == 'H':
            print("\n  Loading high temperatures chart...")
            plot_highs(dates, highs)

        elif choice == 'L':
            print("\n  Loading low temperatures chart...")
            plot_lows(dates, lows)

        elif choice == 'E':
            print("\n  Thank you for using the Sitka Weather Viewer. Goodbye!\n")
            sys.exit(0)

        else:
            print("\n  Invalid selection. Please enter H, L, or E.")


# -- Entry point --
if __name__ == "__main__":
    main()
