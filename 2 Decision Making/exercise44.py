##
# Displays individual present on US banknote
#
one = "George Washington"
two = "Thomas Jefferson"
five = "Abraham Lincoln"
ten = "Alexander Hamilton"
twenty = "Andrew Jackson"
fifty = "Ulysses S. Grant"
hundred = "Benjamin Franklin"

# Read banknote value from user
note = int(input("Enter a banknote value in dollars: "))

# Determine person on banknote
if note == 1:
    person = one
elif note == 2:
    person = two
elif note == 5:
    person = five
elif note == 10:
    person == ten
elif note == 20:
    person = twenty
elif note == 50:
    person = fifty
elif note == 100:
    person = hundred
else:
    person = ""

# Display result
if person == "":
    print("There is no such banknote!")
else:
    print((person + " is on the"), note, "dollar note.")
