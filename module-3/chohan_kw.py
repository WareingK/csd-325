"""chohan_kw.py - Modified Cho-Han game by Kristian Wareing
Original: "Cho-Han" by Al Sweigart al@inventwithpython.com
Source: https://nostarch.com/big-book-small-python-projects

CSD-325 | Assignment 3.2 - Brownfield + Flowchart
Author: Kristian Wareing
Date: 2026-06-21

Changes from original chohan.py:
  1. Input prompt changed from '> ' to 'kw: ' throughout (lines with input())
  2. House fee changed from 10% (pot // 10) to 12% (pot * 12 // 100)
  3. Introduction updated to notify the player about the 2 or 7 dice total bonus
  4. Added bonus logic: if dice1 + dice2 == 2 or 7, player receives 10 mon added to purse
"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

# CHANGE 3: Added bonus notice to the introduction text
print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

BONUS: If the total of the two dice is 2 or 7, you receive a 10 mon bonus!
''')

purse = 5000
while True:  # Main game loop.
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        # CHANGE 1: Updated input prompt from '> ' to 'kw: '
        pot = input('kw: ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            # This is a valid bet.
            pot = int(pot)  # Convert pot to an integer.
            break  # Exit the loop once a valid bet is placed.

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        # CHANGE 1: Updated input prompt from '> ' to 'kw: '
        bet = input('kw: ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Determine if the player won:
    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    # Display the bet results:
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot  # Add the pot to player's purse.
        # CHANGE 2: House fee changed from 10% (pot // 10) to 12% (pot * 12 // 100)
        house_fee = pot * 12 // 100
        print('The house collects a', house_fee, 'mon fee.')
        purse = purse - house_fee  # Deduct the 12% house fee.
    else:
        purse = purse - pot  # Subtract the pot from player's purse.
        print('You lost!')

    # CHANGE 4: Bonus logic — if dice total is 2 or 7, award 10 mon bonus
    dice_total = dice1 + dice2
    if dice_total == 2 or dice_total == 7:
        print(f'Your dice total was {dice_total} -- you get a 10 mon bonus!')
        purse = purse + 10  # Add the 10 mon bonus to the purse.

    # Check if the player has run out of money:
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
