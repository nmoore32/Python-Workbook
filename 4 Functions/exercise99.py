##
# Displays the first prime number larger than a value entered by the user
#
from exercise98 import isPrime

## Determines the first prime number larger than a given integer
# @param n the integer
# @return the first prime number larger than n
#
def nextPrime(n):
    # Set result to one more than the entered value
    result = n + 1
    # Increment result as long as it isn't prime
    while isPrime(result) == False:
        result += 1
    # When a prime number is found, return that number
    return result


# Displays the first prime number larger than a value entered by the user
def main():
    n = int(input("Enter an integer: "))
    print(f"The first prime number larger than {n} is {nextPrime(n)}.")


# Call the main function only if the file has not been imported
if __name__ == "__main__":
    main()

