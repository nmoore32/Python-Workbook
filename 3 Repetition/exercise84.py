##
# Coin flip simulator. Flips coin until it gets three consecutive heads or
# three consecutive tails. Then reports the number of flips taken to get
# these outcomes. Runs the simulation 9 more times, then reports the average
# number of flips needed to get three consective results.
#
from random import randrange

HEADS = 1
TAILS = 2

# Initialize a variable to keep track of the total number of coin flips.
total_num_flips = 0

# For loop to run 10 simulations
for i in range(0, 10):

    # Initialize variables to keep track of last two flip results, the number of flips
    # in a given simulation.
    sl_result = 0
    l_result = 0
    num_flips = 0

    # Simulate coin flips until obtain three consecutive matches
    while True:
        c_result = randrange(HEADS, TAILS + 1)
        # Print out the result of the current coin flip
        if c_result == HEADS:
            print("H", end=" ")
        else:
            print("T", end=" ")

        # Increment the number of flips by 1
        num_flips += 1

        # Check if we have three consecutive matches yet
        if sl_result == l_result == c_result:
            # If so, break the loop
            break
        else:
            # If not
            sl_result = l_result
            l_result = c_result

    # Print the number of flips needed to get three consecutive matches
    print(f"({num_flips} flips)")

    # Add the number of flips from that simulation to the total number of flips
    total_num_flips += num_flips

# Display the average number of flips to get three consecutive matches
print(f"The average number of flips is {total_num_flips / 10}.")

