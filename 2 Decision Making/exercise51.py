##
# Program that computes the roots of a quadratic function
#

# Get values from user
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# Determine the roots
root_one = 0
root_two = 0
discriminant = (b ** 2) - (4 * a * c)

if discriminant < 0:
    print("This quadratic has no real roots.")
elif discriminant == 0:
    root_one = (-b) / (2 * a)
    print(f"This quadratic has one real root equal to {root_one}.")
else:
    root_one = ((-b) + discriminant) / (2 * a)
    root_two = ((-b) - discriminant) / (2 * a)
    print(f"This quadratic has two real roots equal to {root_one} and {root_two}.")

