##
# Creates a copy of a file with line numbers added
#

# Ask the user for a file name
fname = input("Enter a filename: ")

try:
    # Open the file
    inf = open(fname, "r")
    # Open a file for writing
    outf = open("copy_words.txt", "w")

    # Add each line to the new file, prefixed by the line number
    count = 1
    for line in inf:
        outf.write(f"{str(count)}: {line}")
        count += 1
    # Close the files
    inf.close()
    outf.close()

except:
    print("Error accessing file.")
