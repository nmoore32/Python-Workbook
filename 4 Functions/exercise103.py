##
# Displays a message saying whether a randomly generated password is good
#
from exercise102 import checkPassword
from exercise100 import generatePassword


def main():
    # Keep generating random password until a good one is found and display
    # the number of attempts needed to generate it
    count = 0
    while True:
        password = generatePassword()
        if checkPassword(password):
            count += 1
            break
        count += 1

    print(f"It took {count} attempts to generate a good password.")
    print(f"The password is {password}.")


main()

