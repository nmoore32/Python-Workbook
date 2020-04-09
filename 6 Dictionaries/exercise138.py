##
# Displays the keypad sequence needed to type a text message with the numeric keypad.
#

KEY_PRESSES = {
    ".": 1, "A": 2, "D": 3, "G": 4, "J": 5, "M": 6, "P": 7, "T": 8, "W": 9, " ": 0,
    ",": 11, "B": 22, "E": 33, "H": 44, "K": 55, "N": 66, "Q": 77, "U": 88, "X": 99,
    "?": 111, "C": 222, "F": 333, "I": 444, "L": 555, "O": 666, "R": 777, "V": 888, "Y": 999,
    "!": 1111, "S": 7777, "Z": 9999, ":": 11111
}

message = input("Enter a message: ")

for char in message:
    print(KEY_PRESSES[char.upper()], end="")
