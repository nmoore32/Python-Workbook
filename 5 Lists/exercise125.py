##
# Displays a deck of cards before and after it's been shuffled
#
from random import randrange

VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
SUITS = ["s", "c", "d", "h"]


# Creates a standard deck of playing cards
# @return a list of cards
def createDeck():
    # Create a list to hold the cards
    cards = []

    # For each suit and value, construct and add the card to the list
    for suit in SUITS:
        for value in VALUES:
            cards.append(value + suit)

    # Return the complete deck of cards
    return cards


# Shuffles a deck of cards
# @param cards the cards to be shuffles
# @return a list of the the shuffled cards
def shuffle(cards):
    # Go through the cards one by one
    for pos in range(0, len(cards)):
        # Pick a random index between the current index and the end of the list
        new_pos = randrange(pos, len(cards))

        # Swap the current card with the one at the random position
        temp = cards[pos]
        cards[pos] = cards[new_pos]
        cards[new_pos] = temp


# Test the createDeck() and shuffle() functions
def main():
    deck = createDeck()
    print("The original card list: ")
    print(deck)
    print()

    shuffle(deck)
    print("The shuffled card list:")
    print(deck)


if __name__ == "__main__":
    main()
