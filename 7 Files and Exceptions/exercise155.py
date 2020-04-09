##
# Displays the word (or words) that occur most frequently in a file.
#
from exercise117 import getWords


# Get filename from user
fname = input("Enter a filename: ")

try:
    # Open the file
    inf = open(fname)

    # Create a dictionary to store each word the its frequency
    word_freq = {}

    # Process each line in the file
    for line in inf:
        words = getWords(line)
        # Increment the count for each word, adding it to the dictionary if needed
        for word in words:
            if word.lower() not in word_freq:
                word_freq[word.lower()] = 1
            else:
                word_freq[word.lower()] += 1

    # Close the file
    inf.close()

    # Find the max value in the dictionary
    max_v = max(word_freq.values())

    # Display the results
    print(f"The following words occur {max_v} times:")
    for word in word_freq:
        if word_freq[word] == max_v:
            print(word)

except:
    print("Error accessing file.")
