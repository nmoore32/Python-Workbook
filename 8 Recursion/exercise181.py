##
# Determines whether it is possible to construct a particular total using a specific
# number of coins.
#
coins = [25, 10, 5, 1]


# Determine whether it is possible to construct a particular total using a specific number
# of coins.
# @param s dollar amount in cents
# @param n number of coins
# #return True if it's possible, False otherwise
def possibleChange(s, n):
    # Base case
    if s == 0 and n == 0:
        return True
    elif n == 0:
        return False

    # Recursive case
    for coin in coins:
        if n * coin == s:
            return possibleChange(s - coin, n - 1)
    for coin in coins:
        if s > coin:
            return possibleChange(s - coin, n - 1)


# Test possibleChange()
def main():
    s = int(input("Enter a dollar amount: "))
    n = int(input("Enter a number of coins: "))
    if possibleChange(s, n):
        print(f"You can make ${s / 100:.2f} with {n} coins.")
    else:
        print(f"You can't make ${s / 100:.2f} with {n} coins")


if __name__ == "__main__":
    main()
