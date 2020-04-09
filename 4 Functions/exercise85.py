##
# Given the two shorted sides of a right triangle, computes the hypotenuse
#
from math import sqrt

# Define a function to calculate the hypotenuse from the two shorter sides
def hypotenuse(a, b):
    c = sqrt(a ** 2 + b ** 2)
    return c


def main():

    # Read side lengths from user
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))

    print(f"The hypotenuse is {hypotenuse(a, b):.2f}.")


main()

