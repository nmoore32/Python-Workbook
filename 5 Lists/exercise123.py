##
# Displays a string entered by the user in Pig Latin
#
VOWELS = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
UPPERCASE_CONSONANT = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q",
                       "R", "S", "T", "V", "W", "X", "Y", "Z", ]
PUNCTUATION = [",", ".", "?", "!"]
CONSONANT_TAIL = "ay"
VOWEL_TAIL = "way"

# Get string to convert from user and create a list of words in the string
line = input("Enter a string: ")
words = line.split()

# Go through each word in words, convert it to Pig Latin and add it to result
result = []
for word in words:
    # Determine the index of the first vowel
    first_vowel = 0
    for index, char in enumerate(word):
        if char in VOWELS:
            first_vowel = index
            break

    # Create list of punctuation characters and an index for the first punctuation mark
    punctuation = []
    first_punctuation = ""
    for index, char in enumerate(word):
        if char in PUNCTUATION:
            punctuation.append(char)
            if first_punctuation == "":
                first_punctuation = index

    # If the first letter is a vowel, append VOWEL_TAIL to the word
    if first_vowel == 0 and first_punctuation == "":
        word = word + VOWEL_TAIL
    elif first_vowel == 0:
        word = word[:first_punctuation] + VOWEL_TAIL
    # If the first letter is an uppercase consonant construct the Pig Latin conversion
    # with the equivalent lowercase consonant at the end and the first vowel capitalized
    elif word[0] in UPPERCASE_CONSONANT and first_punctuation == "":
        word = (
            word[first_vowel].upper() + word[first_vowel + 1:] + word[0].lower() +
            word[1:first_vowel] + CONSONANT_TAIL
        )
    elif word[0] in UPPERCASE_CONSONANT:
        word = (
            word[first_vowel].upper() + word[first_vowel + 1: first_punctuation] +
            word[0].lower() + word[1:first_vowel] + CONSONANT_TAIL
        )
    elif first_punctuation == "":
        word = word[first_vowel:] + word[:first_vowel] + CONSONANT_TAIL
    else:
        word = word[first_vowel:first_punctuation] + \
            word[:first_vowel] + CONSONANT_TAIL

    # Add any punctuation marks at the end and add the converted word to result
    if punctuation:
        for char in punctuation:
            word = word + char

    # Add the converted word to result
    result.append(word)

# Display the result
for word in result:
    print(word, end=" ")
