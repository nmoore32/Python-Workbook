##
# Determines whether one list is a sublist of another
#

# Determines whether one list is a sublist of another
# @param larger the list to check for the sublist
# @param smaller the sublist to check for
# @return True if smaller is a sublist of large, False otherwise


def isSublist(l, s):
    # If smaller is the empty list or the lists are the same, return True
    if (s == []) or (l == s):
        return True
    # If smaller is longer than larger, return false
    elif len(s) > len(l):
        return False
    # Compare the individual elements
    else:
        for i, item in enumerate(l):
            # When you find the first element of smaller in larger
            if item == s[0]:
                # Check if the rest of the elements of smaller follow in order
                n = 1
                while (n < len(s)) and (l[i + n] == s[n]):
                    n += 1
                # If n equals the length of smaller, then smaller is a sublist of larger
                if n == len(s):
                    return True
        return False

# Demonstrate isSublist function


def main():
    test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    shorter = [3, 4, 5]
    longer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    notsub = [1, 2, 3, 7, 8, 9]

    print(f"Empty list: Result: {isSublist(test, [])}   Expected: True")
    print(f"Identical list: Result: {isSublist(test, test)}  Expected: True")
    print(
        f"Smaller sublist: Result: {isSublist(test, shorter)}  Expected: True")
    print(
        f"Longer sublist: Result: {isSublist(test, longer)}  Expected: False")
    print(f"Not sublist: Result {isSublist(test, notsub)}  Expected: False")


if __name__ == "__main__":
    main()
