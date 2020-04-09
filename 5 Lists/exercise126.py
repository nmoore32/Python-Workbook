##
# Creates a deck cards, shuffles it, and deals out a hand
#
from exercise125 import createDeck, shuffle


# Deals out hands of cards
# @param hands the number of hands of cards
# @param cards the number of cards per hand
# @param deck the deck of cards to be dealt
# @return a list containing all the hands that were dealt
def deal(hands, cards, deck):
    # Create the list of hands to return
    result = []
    # for the number of cards to be dealt, deal a card to each hand
    for i in range(cards):
        for j in range(hands):
            # Create a new list object for the first card dealt to each hanf
            if i == 0:
                result.append([deck.pop(0)])
            else:
                result[j].append(deck.pop(0))
    return result


# Deal out four hands of five cards, display them, and display the remaining cards
def main():
    # Create a deck, shuffle, and deal
    deck = createDeck()
    shuffle(deck)
    hands = deal(4, 5, deck)

    # Print out each hand
    for hand in hands:
        print(hand)
    print()

    # Print the remaining cards in the deck
    print("The remaining cards are: ")
    print(deck)


if __name__ == "__main__":
    main()
