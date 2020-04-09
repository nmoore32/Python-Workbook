##
# Checks if a Bingo card is a winner
#


# Checks if a Bingo card if a winner
# @param card the card to check
# @return True if the card is a winner, False otherwise
def checkCard(card):
    isWinner = False

    # Check for vertical wins (zeros indicate "crossed" out numbers, so winning rows sum to 0)
    sum = 0
    for key in card:
        for i in range(5):
            sum += (card[key])[i]
        if sum == 0:
            isWinner = True
        sum = 0

    # Check for horizontal wins
    sum = 0
    for i in range(5):
        for key in card:
            sum += (card[key])[i]
        if sum == 0:
            isWinner = True
        sum = 0

    # Check for diagonal wins
    if (card["B"][0] + card["I"][1] + card["N"][2] + card["G"][3] + card["O"][4]) == 0:
        isWinner = True
    if (card["B"][4] + card["I"][3] + card["N"][2] + card["G"][1] + card["O"][0]) == 0:
        isWinner = True

    return isWinner


# Test the checkCard function
def main():
    # Card with no wins
    card0 = {'B': [1, 7, 8, 14, 15], 'I': [24, 21, 19, 22, 20], 'N': [32, 35, 40, 45, 31],
             'G': [56, 55, 46, 48, 59], 'O': [70, 69, 68, 66, 64]}

    # Cards with vertical wins
    card1 = {'B': [0, 0, 0, 0, 0], 'I': [24, 21, 19, 22, 20], 'N': [32, 35, 40, 45, 31],
             'G': [56, 55, 46, 48, 59], 'O': [70, 69, 68, 66, 64]}
    card2 = {'B': [13, 6, 1, 12, 7], 'I': [0, 0, 0, 0, 0], 'N': [32, 35, 40, 45, 31],
             'G': [56, 55, 46, 48, 59], 'O': [70, 69, 68, 66, 64]}
    card3 = {'B': [13, 6, 1, 12, 7], 'I': [24, 21, 19, 22, 20], 'N': [0, 0, 0, 0, 0],
             'G': [56, 55, 46, 48, 59], 'O': [70, 69, 68, 66, 64]}
    card4 = {'B': [13, 6, 1, 12, 7], 'I': [24, 21, 19, 22, 20], 'N': [32, 35, 40, 45, 31],
             'G': [0, 0, 0, 0, 0], 'O': [70, 69, 68, 66, 64]}
    card5 = {'B': [13, 6, 1, 12, 7], 'I': [24, 21, 19, 22, 20], 'N': [32, 35, 40, 45, 31],
             'G': [56, 55, 46, 48, 59], 'O': [0, 0, 0, 0, 0]}

    # Cards with horizontal wins
    card6 = {'B': [0, 7, 8, 14, 15], 'I': [0, 21, 19, 22, 20], 'N': [0, 35, 40, 45, 31],
             'G': [0, 55, 46, 48, 59], 'O': [0, 69, 68, 66, 64]}
    card7 = {'B': [1, 0, 8, 14, 15], 'I': [24, 0, 19, 22, 20], 'N': [32, 0, 40, 45, 31],
             'G': [56, 0, 46, 48, 59], 'O': [70, 0, 68, 66, 64]}
    card8 = {'B': [1, 7, 0, 14, 15], 'I': [24, 21, 0, 22, 20], 'N': [32, 35, 0, 45, 31],
             'G': [56, 55, 0, 48, 59], 'O': [70, 69, 0, 66, 64]}
    card9 = {'B': [1, 7, 8, 0, 15], 'I': [24, 21, 19, 0, 20], 'N': [32, 35, 40, 0, 31],
             'G': [56, 55, 46, 0, 59], 'O': [70, 69, 68, 0, 64]}
    card10 = {'B': [1, 7, 8, 14, 0], 'I': [24, 21, 19, 22, 0], 'N': [32, 35, 40, 45, 0],
              'G': [56, 55, 46, 48, 0], 'O': [70, 69, 68, 66, 0]}

    # Cards with diagonal wins
    card11 = {'B': [0, 7, 8, 14, 15], 'I': [24, 0, 19, 22, 20], 'N': [32, 35, 0, 45, 31],
              'G': [56, 55, 46, 0, 59], 'O': [70, 69, 68, 66, 0]}
    card12 = {'B': [1, 7, 8, 14, 0], 'I': [24, 21, 19, 0, 20], 'N': [32, 35, 0, 45, 31],
              'G': [56, 0, 46, 48, 59], 'O': [0, 69, 68, 66, 64]}

    print(f"{checkCard(card0)} Expected: False")
    print(f"{checkCard(card1)} Expected: True")
    print(f"{checkCard(card2)} Expected: True")
    print(f"{checkCard(card3)} Expected: True")
    print(f"{checkCard(card4)} Expected: True")
    print(f"{checkCard(card5)} Expected: True")
    print(f"{checkCard(card6)} Expected: True")
    print(f"{checkCard(card7)} Expected: True")
    print(f"{checkCard(card8)} Expected: True")
    print(f"{checkCard(card9)} Expected: True")
    print(f"{checkCard(card10)} Expected: True")
    print(f"{checkCard(card11)} Expected: True")
    print(f"{checkCard(card12)} Expected: True")


if __name__ == "__main__":
    main()
