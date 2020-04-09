##
# Converts human years to dog years treating the first two human years
# as each equivalent to 10.5 dog years, and each additional human year
# as 4 dog years
#

# Read number of human years from user
years = float(input("Enter dogs age: "))

if (years < 0):
    print("Please enter a positive number.")
elif (years < 2):
    print("The dog is", years * 10.5, "years old in dog years.")
else:
    print("The dog is", 2 * 10.5 + (years - 2) * 4, \
        "years old in dog years.")
