##
# Calculates average of a series of numbers
#

# Gets first value from user
x = float(input("Enter a value ('0' to quit): "))

# Returns error message if first value entered is 0
if x == 0:
    print("Please enter a value other than '0'")

# Initialize variables to keep track of sum of entered values and
# number of entered value
sum = 0
count = 0

# While loop to get values as long as user doesn't enter 0
while x != 0:
    sum += x
    count += 1
    x = float(input("Enter a value ('0' to quit): "))

# Calculate average
average = sum / count

# Displat average
print(f"The average is {average:.2f}.")
