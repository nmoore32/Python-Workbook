##
# Determine the greatest common divisor of two positive integers
#


# Determine the greatest common divisor of two positve integers.
def getGCD(a, b):
    # Base case
    if b == 0:
        return a
    else:
        # Recurvise case
        c = a % b
        return getGCD(b, c)


# Test getGCD function
def main():
    # Read two positive integers from user
    a = int(input("Enter a positive integer: "))
    b = int(input("Enter another positive integer: "))

    gcd = getGCD(a, b)
    print(f"The greatest common denominator is {gcd}")


if __name__ == "__main__":
    main()
