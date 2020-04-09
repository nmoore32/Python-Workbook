##
# Determines whether two strings are anagrams. Now ignores spacing, punctuation, and case.
#
from string import punctuation

# Computer the number of times a given character appears in a string
# @param s the string to examine
# @return a dictionary containing char-count pairs


def characterCounts(s):
    # Create empty dictionary and a lowercase copy of the string with spaces removed
    counts = {}
    s1 = (s.lower()).replace(" ", "")

    # Update the count for each character
    for ch in s1:
        # If the character is a punctuation mark, skip it
        if ch in punctuation:
            continue
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1

    # Return the result
    return counts

# Determine if two strings entered by the user are anagrams


def main():
    # Read two string from the user
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")

    # Get the character counts for each string
    counts1 = characterCounts(s1)
    counts2 = characterCounts(s2)

    # Display the result
    if counts1 == counts2:
        print("Those strings are anagrams.")
    else:
        print("Those strings are not anagrams.")


# Only run the main function if file is not imported
if __name__ == "__main__":
    main()
