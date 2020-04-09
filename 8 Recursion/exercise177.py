##
# Converts a Roman numeral to an integer
#
ROMAN_NUMERALS = {"M": 1000, "D": 500,
                  "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}


# Convert a Roman numeral to an integer
# @param num the Roman numeral to convert
# @return an int containing the integer value of the Roman numeral
def rom2int(num):
    # Base case
    if num == "":
        return 0

    # Calculate the tail
    tail = num[1: len(num)]

    # Recursive case
    # If the next numeral is larger than the current one, subtract the value of the current numeral
    if len(num) > 1:
        if ROMAN_NUMERALS[num[0]] < ROMAN_NUMERALS[num[1]]:
            return rom2int(tail) - ROMAN_NUMERALS[num[0]]
    # Otherwise, add the value of the current numeral
    return rom2int(tail) + ROMAN_NUMERALS[num[0]]


# Test rom2int
def main():
    # Read a Roman numeral from user
    num = input("Enter a Roman numeral: ")
    print(rom2int(num))


if __name__ == "__main__":
    main()
