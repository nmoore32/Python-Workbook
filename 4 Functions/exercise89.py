##
# Converts an integer into an English ordinal number.
#

## Converts an integer into an English ordinal numnber.
def ordinal(n):
    if 1 <= n <= 12:
        if n == 1:
            return "first"
        elif n == 2:
            return "second"
        elif n == 3:
            return "third"
        elif n == 4:
            return "fourth"
        elif n == 5:
            return "fifth"
        elif n == 6:
            return "sixth"
        elif n == 7:
            return "seventh"
        elif n == 8:
            return "eighth"
        elif n == 9:
            return "ninth"
        elif n == 10:
            return "tenth"
        elif n == 11:
            return "eleventh"
        elif n == 12:
            return "twelfth"
    else:
        return ""


# Define main function
def main():
    # Get input from user and display English ordinal
    n = int(input("Enter a integer from 1 to 12: "))

    print(ordinal(n))


# Only run main program if file wasn't imported
if __name__ == "__main__":
    main()
