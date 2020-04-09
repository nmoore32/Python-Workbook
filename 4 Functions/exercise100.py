##
# Generate and display a random password between 7 and 10 characters
#
from random import randint

SHORTEST = 7
LONGEST = 10
MIN_ASCII = 33
MAX_ASCII = 126

## Generates a random password of 7 to 10 characters
# @return a string containing a random password
def generatePassword():
    # Select random length for password
    randomLength = randint(SHORTEST, LONGEST)

    # Select the appropriate number of characters, adding them to the result
    result = ""
    for i in range(randomLength):
        randomChar = randint(MIN_ASCII, MAX_ASCII)
        result = result + chr(randomChar)

    # Return the random password
    return result


# Displays a randomly generated password
def main():
    print(f"Your random password is: {generatePassword()}")


# Run main only if not imported
if __name__ == "__main__":
    main()
