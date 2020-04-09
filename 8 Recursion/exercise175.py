##
# Convert a decimal number to its binary representation.
#


# Convert a decimal number to its binary representation.
# @param n the decimal number to convert
# @return a string containing the binary representation of n
def dec2bin(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case
        return f"{dec2bin(n // 2)}{n % 2}"


# Test the dec2bin function
def main():
    # Read a decimal number to convert from user
    n = int(input("Enter a number: "))

    # Display the result
    print(dec2bin(n))


if __name__ == "__main__":
    main()
