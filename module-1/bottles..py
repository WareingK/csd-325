# Author: Kristian Wareing
# Date: June 7, 2026
# Assignment: CSD-325 Module 1 - On the Wall

# Purpose: Count down bottles of beer on the wall from a user-specified number to 1,
# displaying the classic song lyrics, then prompt the user to buy more beer.


def countdown(bottles):
    # Count down from the given number to 1, displaying lyrics for each number
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        bottles -= 1
        print(
            f"Take one down and pass it around, {bottles} bottle{'s' if bottles > 1 else ''} of beer on the wall.\n"
        )

    # Display the final verse with singular "bottle"
    print("1 bottle of beer on the wall, 1 bottle of beer.")
    print("Take one down and pass it around, no more bottles of beer on the wall.\n")


def main():
    # Ask the user how many bottles to start with
    user_input = input("How many bottles of beer are on the wall? ")

    # Validate that the input is a positive integer
    if not user_input.isdigit() or int(user_input) < 1:
        print("Please enter a positive whole number.")
        return

    bottles = int(user_input)

    # Pass the input to the countdown function
    countdown(bottles)

    # Return to main program and remind the user to buy more beer
    print("Time to buy more beer!")


main()
