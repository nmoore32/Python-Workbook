##
# Reads a list of numbers from the user and tells them if the list is sorted or not
#


# Determines whether a list is sorted
# @param numbers the list of numbers to be checked
# @return True is the list is sorted (or empty, or only has one element), False otherwise
def isSorted(numbers):
    isAscending = True
    isDescending = True
    # For each number, check if it's larger or smaller than the next
    for i in range(1, len(numbers)):
        # If smaller then not in ascending order. If larger then not in descending order
        if numbers[i] < numbers[i - 1]:
            isAscending = False
        if numbers[i] > numbers[i - 1]:
            isDescending = False
    if isAscending or isDescending:
        return True
    return False


# Ask user for a list of numbers then reports if they are sorted
def main():
    numbers = []
    line = input("Enter a number (blank to stop): ")
    while line != "":
        num = int(line)
        numbers.append(num)
        line = input("Enter a number (blank to stop): ")
    if isSorted(numbers):
        print("The numbers are sorted.")
    else:
        print("The numbers are not sorted.")


if __name__ == "__main__":
    main()
