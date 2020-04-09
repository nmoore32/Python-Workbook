##
# Reads a text file and displays the contents using consistent line lengths.
#

MAX_LINE_LENGTH = 50

# Get file name to display from user
fname = input("Enter a filename: ")

try:
    inf = open(fname)
except:
    print("Error opening file.")
    print("Quitting...")
    quit()

# Make a list of all the words in the file
try:
    words_inf = []
    for line in inf:
        words = line.split(" ")
        for word in words:
            if word == "\n":
                words_inf.append(word)
            else:
                words_inf.append(word.rstrip())
    # Close the file
    inf.close()

    # Construct lines of MAX_LINE_LENGTH and display them
    line = ""
    while words_inf:
        # If the next word can be added to a line without going over limit, add it to the line
        if words_inf[0] != "\n" and (len(line + " " + words_inf[0]) <= MAX_LINE_LENGTH):
            line = line + " " + words_inf[0]
            # Remove each word that has been added to line from the list of words
            words_inf.pop(0)
        # If the next "word" is a newline character, prine the current line and a blank line
        elif words_inf[0] == "\n":
            print(line)
            print()
            # Reset line to blank after printing a line
            line = ""
            # Remove the newline character from the list of words after printing a blank line
            words_inf.pop(0)
        # If the next word can't be added without going over the limit or there is no next word
        # print the current line and reset it to blank
        else:
            print(line)
            line = ""

    # If line isn't blank after the last iteration of the while loop, print the remaining line
    if line != "":
        print(line)

except:
    print("Error reading file.")
    print("Quitting...")
    quit()
