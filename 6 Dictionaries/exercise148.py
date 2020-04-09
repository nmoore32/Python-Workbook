##
# Simulate a Bingo game for a single Bingo card
#
from random import shuffle
from exercise146 import createBingo, displayBingo
from exercise147 import checkCard

NUMs_PER_LETTER = 15


# Simulate a Bingo game for a single Bingo card
# @return an integer representing the number of calls needed for the win
def simulateBingo():
    # Generate a list of all valid Bingo calls
    calls = []

    # Set upper and lower ranges for the numbers to be selected from
    lower = 1
    upper = NUMs_PER_LETTER + 1
    # For each letter, generate all valid Bingo calls for that letter and add them to the list
    for letter in ["B", "I", "N", "G", "O"]:
        for i in range(lower, upper):
            calls.append(f"{letter}{i}")
        # Set the limits for the next letter
        lower += NUMs_PER_LETTER
        upper += NUMs_PER_LETTER

    # Shuffle the list
    shuffle(calls)

    # Create a Bingo card
    card = createBingo()

    # Call numbers from calls, crossing them off the card, until we have a win
    while not checkCard(card):
        # Call the next number from calls and remove it from the list
        call = calls.pop(0)
        # Check if there's a matching number on the card, if so set it to 0
        for i, v in enumerate(card[call[0]]):
            if v == int(call[1:]):
                card[call[0]][i] = 0

    # Return the number of calls needed for the win
    return (75 - len(calls))

# Simulate 1000 Bingo games and report the minimum, maximum, and average number of calls
# needed for the win


def main():
    # Create a list to store the result in
    results = []

    # Simulate the 1000 games and store the results
    for i in range(1000):
        results.append(simulateBingo())

    # Calculate the average number of calls needed
    total_calls = 0
    for num in results:
        total_calls += num
    average = (total_calls / 1000)

    # Return the results
    print(f"The minimum number of calls needed was {min(results)}.")
    print(f"The maximum number of calls needed was {max(results)}.")
    print(f"The average number of calls needed was {average:.0f}.")


# Only run the main function when file not imported
if __name__ == "__main__":
    main()
