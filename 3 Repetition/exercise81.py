##
# Converts a binary number into a decimal
#

# Read binary number from user
number = input("Enter a binary number: ")

# Track contribution to decimal from each bit
decimal = 0

# Convert to decimal
i = len(number) - 1
while i > -1:
    if number[i] == "1":
        decimal += 2 ** (len(number) - 1 - i)
    i -= 1

# Display result
print(f"The decimal representation of {number} is {decimal}.")

