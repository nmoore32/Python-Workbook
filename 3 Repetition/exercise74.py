##
# Uses Newton's method to approximate a square root
#

# Ask for a number
x = float(input("Enter a number: "))

# Initialize guess
guess = x / 2

while abs(guess * guess - x) > 10e-12:
    guess = (guess + x / guess) / 2

print(guess)

