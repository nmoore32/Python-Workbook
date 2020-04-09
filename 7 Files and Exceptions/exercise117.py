# Note: Modified to check for punctuation using the string class

##
# Displays a list of the words in a string provided by the user.
#
from string import punctuation


# Makes a list of words from a given string
# @param the string to make the list from
# @return a list containing all the words in the given string
def getWords(string):
    # Make a list of all punctuation marks we would like to remove
    #    punctuation = [",", ".", "?", "-", "'", "!", ":", ";"]

    # Make a list to store return value
    retval = []

    # Go through the string adding words to retval
    initial_pos = 0
    # If index is pointing to a character that indicates the end of a word,
    # add the string deliminted by [initial_pos, index) to the list as long as
    # it isn't empty
    for index, char in enumerate(string):
        if (
            (char in punctuation and char != "'")
            or (char == "'" and index == len(string) - 1)
            or char == " "
        ):
            if string[initial_pos:index] != "":
                retval.append(string[initial_pos:index])
            initial_pos = index + 1
        elif char == "'" and string[index + 1] == " ":
            if string[initial_pos:index] != "":
                retval.append(string[initial_pos:index])
            initial_pos = index + 1
        elif index == len(string) - 1:
            if string[initial_pos: index + 1] != "":
                retval.append(string[initial_pos: index + 1])

    return retval


# Display a list of words in a string entered by the user
def main():
    line = input("Enter a string: ")
    words = getWords(line)
    for word in words:
        print(word)


if __name__ == "__main__":
    main()
