##
# Searches a file containing a list of words for any words that contain each of the vowels,
# including Y, exactly once and in order.
#
VOWELS = ["a", "e", "i", "o", "u", "y"]

# Read file to search from user
inf_name = input("Enter a file to search: ")

# Open the file, providing an error message if a problem is encounted
try:
    inf = open(inf_name)
except:
    print("Error opening file.")
    print("Quitting...")
    quit()

# Search each line for words meeting out criteria and add them to matches
try:
    matches = []
    for line in inf:
        words = line.split(" ")
        for word in words:
            # Make a list of each vowel in the word in order, including duplicates
            vowels = []
            word = word.lower()
            for ch in word:
                if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u" or ch == "y":
                    vowels.append(ch)
            # If the list of vowels equals VOWELS, we've found a word matching our criteria
            if vowels == VOWELS:
                matches.append(word.rstrip())

    # Close the file
    inf.close()

except:
    print("Error reading file.")

# Display the results
if matches:
    print("The following words contain all of the vowels, including y, exactly once and in order:")
    for word in matches:
        print(f" - {word}")
else:
    print("There are no matching words in the file provided.")
