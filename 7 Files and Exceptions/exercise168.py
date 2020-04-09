##
# Reads a file and reports repeated words.
#
import sys

from exercise117 import getWords

# Check for the appropriate number of command line arguments
if len(sys.argv) != 2:
    print("Please enter a filename!")
    print("Quitting...")
    quit()

# Open the file
try:
    inf = open(sys.argv[1])
except:
    print("Error accessing file.")
    print("Quitting...")
    quit()

# Run through each line of the file checking for repeated words. Add those words to a list
# along with the line number
repeated = []
# Run through each line using enumerate for the index number
for i, line in enumerate(inf):
    # Split each line into a list of words
    words = getWords(line)
    for j in range(1, len(words)):
        # For each list of words, check if each word is identical to the preceding word. If so
        # add it to the list of repeated words, prefixed by the line number
        if words[j].lower() == words[j - 1].lower():
            repeated.append(f"{i + 1} {words[j]}")

# Close the file
inf.close()

# Report the results
if len(repeated) == 0:
    print("There were no repeated words.")
else:
    print("The repeated words, including line number were:")
    for word in repeated:
        print(f" {word}")
