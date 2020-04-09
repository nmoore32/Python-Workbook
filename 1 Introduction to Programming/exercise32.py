##
# Takes a four-digit integer and displays the sum of the digits
#

# Get integer from user
num = int(input("Enter a four-digit integer:"))

# Determine the digits
d1 = num // 1000
d2 = num // 100 % 10
d3 = num // 10 % 10
d4 = num % 10

# Calculate sum
sum = d1 + d2 + d3 + d4

# Display the result
print(d1, "+", d2, "+", d3, "+", d4, "=", sum)


