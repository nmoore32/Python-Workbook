##
# Finds the longest word(s) in a file, displays the length, and all the words of that length
#

fname = input("Enter a file name: ")

try:
    # Open the file
    inf = open(fname)

    # Make a list of all the words in the file
    words = (inf.read()).split()

    # Close the file
    inf.close()

    # Find the longest word in the list
    length = 0
    for word in words:
        if len(word) > length:
            length = len(word)

    # Store all the words of that length in a new list
    long_words = []
    for word in words:
        if len(word) == length:
            long_words.append(word)

    # Display the results
    print(f"The longest word has {length} letters.")
    print("The words are: ")
    for word in long_words:
        print(word)

except:
    print("Error accessing file.")
