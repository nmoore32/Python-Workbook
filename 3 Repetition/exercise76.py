##
# Determines whether a word or phrase is a palindrome while ignoring spaces and
# punctuation
#

# Import punctuation from the string module to check for punctuation characters
from string import punctuation

# Read input from user
line = input("Enter a word or phrase: ")

# Set variable to track palindrome status
is_palindrome = True

# Make a lowercase copy of the original string so we can ignore case
line_lower = line.lower()

# Check the characters starting from the ends
i = 0
k = len(line) - 1
while i < k:
    if line_lower[i] in punctuation or line_lower[i] == " ":
        i += 1
    if line_lower[k] in punctuation or line_lower[k] == " ":
        k -= 1
    else:
        if line_lower[i] != line_lower[k]:
            is_palindrome = False
        else:
            i += 1
            k -= 1

# Display message
if is_palindrome:
    print(f"{line} is a palindrome.")
else:
    print(f"{line} is not a palindrome.")
