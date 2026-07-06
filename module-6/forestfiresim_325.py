"""Forest Fire Sim, modified by Sue Sampson, based on a program by Al Sweigart
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
** use spaces, not indentation to modify **
Tags: short, bext, simulation

Module 6.2 Update:
Added a permanent lake feature near the center of the forest.
The lake uses the ~ character, displays in blue, and acts as a firebreak.
Water cannot burn, grow trees, or be changed by the simulation.
"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
WATER = '~'  # Module 6.2: Water/lake character. Not A or @.

# Simulation settings:
INITIAL_TREE_DENSITY = 0.20  # Amount of forest that starts with trees.
GROW_CHANCE = 0.01  # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.01  # Chance a tree is hit by lightning and burns.
PAUSE_LENGTH = 0.5

# Module 6.2 lake settings.
# The lake is placed roughly in the center of the display.
LAKE_WIDTH = 7
LAKE_HEIGHT = 5
LAKE_START_X = (WIDTH // 2) - (LAKE_WIDTH // 2)
LAKE_START_Y = (HEIGHT // 2) - (LAKE_HEIGHT // 2)


def main():
    forest = createNewForest()
    bext.clear()

    while True:  # Main program loop.
        displayForest(forest)

        # Run a single simulation step:
        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    # If we've already set nextForest[(x, y)] on a
                    # previous iteration, just do nothing here:
                    continue

                # Module 6.2: Keep water unchanged.
                # The lake acts as a firebreak and cannot be modified.
                if forest[(x, y)] == WATER:
                    nextForest[(x, y)] = WATER
                    continue

                if ((forest[(x, y)] == EMPTY)
                    and (random.random() <= GROW_CHANCE)):
                    # Grow a tree in this empty space.
                    nextForest[(x, y)] = TREE

                elif ((forest[(x, y)] == TREE)
                    and (random.random() <= FIRE_CHANCE)):
                    # Lightning sets this tree on fire.
                    nextForest[(x, y)] = FIRE

                elif forest[(x, y)] == FIRE:
                    # This tree is currently burning.
                    # Loop through all the neighboring spaces:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            # Fire spreads only to neighboring trees.
                            # Water is ignored, so it works as a firebreak.
                            if forest.get((x + ix, y + iy)) == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE

                    # The tree has burned down now, so erase it:
                    nextForest[(x, y)] = EMPTY

                else:
                    # Just copy the existing object:
                    nextForest[(x, y)] = forest[(x, y)]

        forest = nextForest

        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Returns a dictionary for a new forest data structure."""
    forest = {'width': WIDTH, 'height': HEIGHT}

    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Module 6.2: Add a permanent lake in the center.
            # Water cannot burn, grow trees, or be replaced.
            if (LAKE_START_X <= x < LAKE_START_X + LAKE_WIDTH and
                    LAKE_START_Y <= y < LAKE_START_Y + LAKE_HEIGHT):
                forest[(x, y)] = WATER

            elif (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE  # Start as a tree.

            else:
                forest[(x, y)] = EMPTY  # Start as an empty space.

    return forest


def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)

    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')

            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')

            elif forest[(x, y)] == WATER:
                bext.fg('blue')
                print(WATER, end='')

            elif forest[(x, y)] == EMPTY:
                print(EMPTY, end='')

        print()

    bext.fg('reset')  # Use the default font color.
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


# If this program was run instead of imported, run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()