# #
# Determines whether a triangle can be formed from three specified lengths
#

##
# Determines whether a triangle can be formed from three specified lengths
# @param a the first length
# @param b the second length
# @param c the third length
# @return a Boolean value
def isTriangle(a, b, c):
    # Return false if any length entered is negative or zero
    if a <= 0 or b <= 0 or c <= 0:
        return False

    # Check if the lengths can form a triangle
    if a >= (b + c) or b >= (a + c) or c >= (a + b):
        return False
    else:
        return True


# Demonstrate the isTriangle function
def main():
    # Read lengths from user
    a = float(input("Enter the length of the first side: "))
    b = float(input("Enter the length of the second side: "))
    c = float(input("Enter the length of the third side: "))

    # Print the result of the isTriangle function
    print(isTriangle(a, b, c))


if __name__ == "__main__":
    main()
