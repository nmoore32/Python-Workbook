##
# Displays the average of a number of values entered by the user, followed by
# all the below average values, average values, and above average values.
#

# Initialize variable to store entered values
values = []

# Ask the user for another value until a blank line is entered
line = input("Enter a value (blank to stop): ")
while line != "":
    value = float(line)
    values.append(value)
    line = input("Enter a value (blank to stop): ")

# Calculate and display the average
sum = 0
for value in values:
    sum += value
average = sum / len(values)
print(f"The average is: {average:.2f}")

# Print the below average values
print("The below average values are: ", end="")
for value in values:
    if value < average:
        print(value, end="   ")

# Print the average values
if average in values:
    print("\nThe average values are: ", end="")
    for value in values:
        if value == average:
            print(value, end="   ")

# Print the above average values
print("\nThe above average values are: ", end="")
for value in values:
    if value > average:
        print(value, end="   ")
