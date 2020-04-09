##
#
#
#from string import startswith

ELEMENT_FILE = "elements.txt"

# Create lists of element symbols and element names from ELEMENT_FILE
element_symbols = []
element_names = []
inf = open(ELEMENT_FILE)

for line in inf:
    parts = line.split(',')
    element_symbols.append(parts[1])
    element_names.append(parts[2].rstrip())


# Determines whether a word can be spelled with just using element symbols.
# @paramv word the word to be checked
# @return a string with the word spelled with element symbols
def elementSpell(s):
    # Base case
    if s == "":
        return ""

    # Recursive case
    for element_symbol in element_symbols:
        if s.title().startswith(element_symbol):
            return element_symbol + elementSpell(s[len(element_symbol):])
    return ""


# Display any element names that be spelled using only element symbols along with those symbols
def main():
    # Call elementSpell() on each element name
    for name in element_names:
        if len(name) == len(elementSpell(name)):
            print(f"{name} can be be spelled as {elementSpell(name)}")


if __name__ == "__main__":
    main()
