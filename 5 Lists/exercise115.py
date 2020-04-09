##
# Displays a list of proper divisors for a positive integer entered by the user.
#

## Determine the list of proper divisors of a positive integer
# @param n the integer whose divisors we want
# @return a list containing all the divisors of the given integer
def getDivisors(n):
    # Initialize list to store return value
    retval = []

    # Check for divisors and add them to the list
    for i in range(1, n):
        if n % i == 0:
            retval.append(i)

    # Return the result
    return retval


# Display a list of proper divisors for a positive integer entered by the user
def main():
    num = int(input("Enter a positive integer: "))

    # Get the list of divisors
    divisors = getDivisors(num)

    # Display each divisor
    print("The proper divisors of {num} are: ")
    for divisor in divisors:
        print(divisor)


# Call the main function only if the file has not been imported
if __name__ == "__main__":
    main()
