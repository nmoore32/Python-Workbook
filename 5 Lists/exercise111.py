##
# Reads integers from user and then displays them in reverse order
#

# Start with an empty list
data = []

# Read integers from user until they enter zero
num = int(input("Enter an integer (0 to quit): "))
while num != 0:
    data.append(num)
    num = int(input("Enter an integer (0 to quit): "))

# Reverse the list
data.reverse()

# Display the numbers in reverse order
for num in data:
    print(num)

