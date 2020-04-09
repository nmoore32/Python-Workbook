##
# Reports whether a password entered by the user is a good one
#

## Determines whether a password is good. A good password is at least 8
# characters long and contains at least one uppercase letter, at least one
# lower case letter, and at least one number.
# @param p the password to check
# @return True if the password is good, false otherwise
def checkPassword(password):
    has_upper = False
    has_lower = False
    has_num = False

    # Check each character in the password to see if it meets any requirements
    for char in password:
        if "A" <= char <= "Z":
            has_upper = True
        elif "a" <= char <= "z":
            has_lower = True
        elif "0" <= char <= "9":
            has_num = True

    # If the password has all properties, return True
    if has_upper and has_lower and has_num and len(password) >= 8:
        return True
    # If the password is missing one, or more, properties, return False
    return False


# Reports whether a password entered by the user is a good one
def main():
    password = input("Enter a password: ")

    if checkPassword(password):
        print(f"That's a good password!")
    else:
        print(f"That's not a good password.")


if __name__ == "__main__":
    main()
