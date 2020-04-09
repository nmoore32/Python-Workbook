##
# Determines whether a string entered by the user is an integer
#

# Determines whether a string represents an integer
# @param s the string to test
# @return True if it represents an integer and False otherwise
#


def isInteger(s):
    # Remove any leading or trailing whitespace
    s = s.strip(" ")

    # Determine if the remaining characters form an integer
    if (s[0] == "+" or s[0] == "-") and s[1:0].isdigit():
        return True
    if s.isdigit():
        return True
    return False


# Demonstrate the isInteger function
def main():
    s = input("Enter a string: ")
    if isInteger(s):
        print("The string represents an integer.")
    else:
        print("That string does not represent an integer.")


if __name__ == "__main__":
    main()
