##
# Convert an integer into English words
#
ONES = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
        9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
TENS = {2: "twenty", 3: "thirty", 4: "fourty", 5: "fifty", 6: "sixty", 7: "seventy",
        8: "eighty", 9: "ninety"}

# Convert an integer into English words
# @param n the integer to convert
# @return a string containing the integer value in English words


def int2eng(n):
    # Create a string to return
    result = ""

    # Handle the case where n = 0
    if n == 0:
        return "zero"

    # If there is a digit in the hundreds place, add its English value to the string
    if (n // 100) != 0:
        result = result + ONES[n // 100] + " hundred"
        # Set n equal to the remainder to move onto the tens place
        n = n % 100

    # If there is a digit in the tens place greater than 1, add its English value to the string
    if ((n // 10) != 0) and ((n // 10) != 1):
        result = result + " " + TENS[n // 10]
        # Set n equal to the remainder to move on to the ones place
        n = n % 10

    # If the digit in the tens place is 1, add its English value to the string
    if (n // 10) != 0 and ((n // 10) == 1):
        result = result + " " + ONES[n]
        # Set n = 0 to skip the ones place
        n = 0

    # If there's a ones place digit left to account for, add its English value to the string
    if n % 10 != 0:
        result = result + " " + ONES[n % 10]

    # Return the result
    return result


# Demonstrate the int2eng function
def main():
    num = int(input("Enter an integer (between 0 and 999): "))
    print(int2eng(num))


# Only run the main function if the file is not imported
if __name__ == "__main__":
    main()
