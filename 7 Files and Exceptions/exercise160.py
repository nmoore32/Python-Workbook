##
# Determines how many words in a file follow or violate the 'I before E except after C' rule
#
from exercise117 import getWords

# Read the filename to check from the user
fname = input("Enter a filename: ")

# Open the file, printing an error message if something goes wrong
try:
    inf = open(fname)
except:
    print("Error accessing file.")
    print("Quiting...")
    quit()

# Go through each line in the file looking for words that contain "EI" or "IE"
followed = []
violated = []

try:
    for line in inf:
        words = getWords(line.rstrip())
        for word in words:
            word = word.lower()
            if "cei" in word:
                followed.append(word)
            elif "ei" in word or "cie" in word:
                violated.append(word)
            elif "ie" in word:
                followed.append(word)

    # Close the file
    inf.close()

except:
    inf.close()
    print("Error reading file.")
    print("Quitting...")
    quit()

# Display the results
print(f"I before E except after C was followed {len(followed)} times and violated "
      f"{len(violated)} times.")
