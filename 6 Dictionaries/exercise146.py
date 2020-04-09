##
# Creates and displays a random Bingo card (without free space)
#
from random import randrange

NUMS_PER_LETTER = 15


# Creates a random Bingo card
# @return a dictionary containing B I N G O as keys and lists of 5 numbers as values
def createBingo():
    # Create empty dictionary
    card = {}

    # Variables to track the range of values for the current letter
    lower = 1
    upper = 1 + NUMS_PER_LETTER

    # For each of the five letters
    for letter in ["B", "I", "N", "G", "O"]:
        # Create an empty list to the store the generated values
        card[letter] = []

        # Generate five unique values and add them to the list
        while len(card[letter]) < 5:
            next_num = randrange(lower, upper)
            if next_num not in card[letter]:
                card[letter].append(next_num)

        # Update the range values for the next letter
        lower += NUMS_PER_LETTER
        upper += NUMS_PER_LETTER

    # Return the result
    return card


# Displays a Bingo card
# @param card the card to display
# @return (None)"""
def displayBingo(card):
    for key in card:
        print(f" {key}", end="     ")
    print()

    i = 0
    while i < 5:
        for value in card.values():
            print(f"{value[i]:2d}", end="     ")
        print()
        i += 1


# Generage a display a random Bingo card
def main():
    card = createBingo()
    displayBingo(card)


if __name__ == "__main__":
    main()
