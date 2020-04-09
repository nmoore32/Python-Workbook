##
# Provides additional information about an element given its atomic number, name, or symbol.
#

ELEMENTS_FILE = "elements.txt"

# Create lists of atomic numbers and element symbols/names from file.
atomic_numbers = []
symbols = []
names = []
inf = open(ELEMENTS_FILE)

# The file format is atomic_number,symbol,name - so we can split it at commas and add the items
# to the appropriate list
for line in inf:
    items = line.split(",")
    atomic_numbers.append(items[0])
    symbols.append(items[1])
    names.append(items[2].rstrip())

# Close the file
inf.close()

# Return information about the relevant element until user enters blank line
line = input("Enter a number, symbol, or name for an element (blank to quit): ")
while line != "":
    # Make the input title case to compare with the lists of names and symbols
    line = line.title()
    # If the user entered an element name, find its index and the return the appropriate info
    if line in names:
        for i, name in enumerate(names):
            if line == name:
                print(
                    f"{line} ({symbols[i]}) has {atomic_numbers[i]} protons.")
    # If the user entered an element symbol, find its index and return the appropriate info
    elif line in symbols:
        for i, symbol in enumerate(symbols):
            if line == symbol:
                print(f"{line} ({names[i]}) has {atomic_numbers[i]} protons.")
    # If the user entered an atomic number, find its index and return the appropriate info
    elif line in atomic_numbers:
        i = int(line) - 1
        print(f"{names[i]} ({symbols[i]}) has {line} protons.")
    # If the user entered anything else, indicate that the input wasn't valid
    else:
        print("Invalid input.")

    # Ask for the next line
    line = input(
        "Enter a number, symbol, or name for an element (blank to quit): ")
