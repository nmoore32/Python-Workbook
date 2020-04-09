##
# Generates and displays a random license plate that either:
# (1) is three letters followed by three digits
# (2) is four digits followed by three digits
#
from random import randint

MIN_ASCII_LETTERS = 65
MAX_ASCII_LETTERS = 90
MIN_ASCII_NUMBERS = 48
MAX_ASCII_NUMBERS = 57

## Generates a random license plate that either:
# (i) is three letters followed by three digits
# (2) is four digits followed by three characters
# @return a string containing the randomly generated licence plate
def randomLicense():
    # Determine which license format to use
    license_format = randint(1, 2)

    # Generate the appropriate number of random characters, adding them to the result
    result = ""
    if license_format == 1:
        for i in range(3):
            randomChar = chr(randint(MIN_ASCII_LETTERS, MAX_ASCII_LETTERS))
            result = result + randomChar
        for i in range(3):
            randomDigit = chr(randint(MIN_ASCII_NUMBERS, MAX_ASCII_NUMBERS))
            result = result + randomDigit
        return result
    else:
        for i in range(4):
            randomChar = chr(randint(MIN_ASCII_NUMBERS, MAX_ASCII_NUMBERS))
            result = result + randomChar
        for i in range(3):
            randomChar = chr(randint(MIN_ASCII_LETTERS, MAX_ASCII_LETTERS))
            result = result + randomChar
        return result


# Demonstrate randomLicense function
def main():
    print(randomLicense())


if __name__ == "__main__":
    main()

