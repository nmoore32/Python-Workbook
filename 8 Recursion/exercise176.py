##
# Displays the NATO phonetic alphabet spelling of a word.
#
NATO_ALPH = {"A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo", "F": "Foxtrot",
             "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliet", "K": "Kilo", "L": "Lima",
             "M": "Mike", "N": "November", "O": "Oscar", "P": "Papa", "Q": "Quebec", "R": "Romeo",
             "S": "Sierra", "T": "Tango", "U": "Uniform", "V": "Victor", "W": "Whiskey",
             "X": "Xray", "Y": "Yankee", "Z": "Zulu"}


# Determines the Nato phonetic alphabet spelling of a word.
# @param word the word to be examined
# @return a string containing the Nato phonetic alphabet spelling of the word
def getNatoSpelling(word):
    # Base case
    if word == "":
        return ""

    # Compute the tail of word
    tail = word[1: len(word)]

    # Recursive cases
    return f"{NATO_ALPH[word[0].upper()]} {getNatoSpelling(tail)}"


# Test getNatoSpelling()
def main():
    # Read word from user
    word = input("Enter a word: ")
    print(getNatoSpelling(word))


if __name__ == "__main__":
    main()
