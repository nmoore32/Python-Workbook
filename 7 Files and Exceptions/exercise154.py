##
# Determines and displays the frequency of all the letters in a file
#

fname = input("Enter a filename: ")

try:
    # Open the file
    inf = open(fname)

    # Store the contents of the file in a list
    lines = inf.read()

    # Close the file
    inf.close()

    # Make a dictionary to store character counts
    num_chars = {}

    # Loop through all the characters
    for line in lines:
        for char in line:
            if ("A" <= char.upper() <= "Z") and (char.upper() not in num_chars):
                num_chars[char.upper()] = 1
            elif ("A" <= char.upper() <= "Z"):
                num_chars[char.upper()] += 1

    # Display the results
    for k, v in sorted(num_chars.items()):
        print(f"{k} appeared {v} times.")

except:
    print("Error accessing file.")
