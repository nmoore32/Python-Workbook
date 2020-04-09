##
# Approximate a square root through recursion.
#


# Calculate a square root by recursion
# @param n the number whose square root we want
# @param guess the current guess for the square root (default value 1.0)
def getSquareRoot(n, guess=1.0):
    # Base case
    if abs(n - guess ** 2) < 10e-12:
        return guess

    # Recursive case
    new_guess = (guess + n / guess) / 2
    return getSquareRoot(n, new_guess)


# Demonstrate getSquareRoot
def main():
    for i in range(11):
        print(getSquareRoot(i))


if __name__ == "__main__":
    main()
