##
# Translates a string into Morse Code
#
MORSE_CODE = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
              "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
              "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
              "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
              "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--",
              "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..",
              "9": "----."}

# Read input from user
message = (input("Enter a message to be translated: ")).upper()

for char in message:
    if char in MORSE_CODE:
        print(MORSE_CODE[char], end=" ")
