##
# Displays the color of a square on a chessboard given the squares position
#

# Read positon from user
position = input("Enter a chessboard position (e.g. c4): ")

# Store the column and row in different variables
column = position[0]
row = int(position[1])

# Determine the color of the first square in the column
if column == "a" or column == "c" or column == "e" or column == "g":
    first = "black"
else:
    first = "white"

# Determine the color of the selected square
if row % 2 == 0 and first == "black":
    square = "white"
else:
    square = "black"

# Display result
print("The square is " + square + ".")
