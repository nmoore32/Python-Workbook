##
# Detemines if number entered by user is prime
#

## Determines if an integer is prime
# @param n the integer to test
# @return True if n is prime, false otherwise
#
def isPrime(n):
    if n <= 1:
        return False

    # Check each number from 2 to n - 1 to see if it divides evenly into n
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# Demonstrate the isPrime functon
def main():
    n = int(input("Enter an integer: "))
    if isPrime(n):
        print(f"{n} is prime.")
    else:
        print(f"{n} is not prime.")


# Call the main function only if the file has not been imported
if __name__ == "__main__":
    main()
