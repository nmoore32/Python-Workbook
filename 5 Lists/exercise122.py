##
# Displays a string entered by the user in Pig Latin
#
VOWELS = ["a", "e", "i", "o", "u"]
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

    # If the first letter is a vowel, append VOWEL_TAIL to the word
    if first_vowel == 0:
        result.append(word + VOWEL_TAIL)
    else:
        word = word[first_vowel:] + word[:first_vowel]
        result.append(word + CONSONANT_TAIL)

for word in result:
    print(word, end=" ")

