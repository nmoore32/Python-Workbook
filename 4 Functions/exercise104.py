##
# Functions the convert between hexadecimal and decimal integers.
#

## Converts a hexadecimal digit to a decimal integer.
# @param h the hexadecimal string to convert
# @return the resulting integer
def hex2int(h):
    # If the hexidecimal and decimal representations are the same, return int(h)
    if "0" <= h <= "9":
        return int(h)
    # If the hexidecimal digit is from A/a to F/f return the corrsponding integer
    elif "A" <= h <= "F":
        return ord(h) - ord("A") + 10
    elif "a" <= h <= "f":
        return ord(h) - ord("a") + 10
    # Otherwise return error message
    else:
        return "That's not a hexidecimal digit."


## Converts an integer to a hexadecimal digit
# #param n the integer to convert
# return a string containing the hexidecimal digit
def int2hex(n):
    # If the hexidecimal and decimal representations are the same return str(n)
    if 0 <= n <= 9:
        return str(n)
    # If the integer is from 10 to 15 return the corresponding hexidecimal digit
    elif 10 <= n <= 15:
        return chr(n - 10 + ord("A"))
    else:
        return "That's integer doesn't correspond to a single hexidecimal digit."


# Test the functions
def main():
    for i in range(10):
        print(hex2int(str(i)))
        print(int2hex(i))
    print()
    for i in range(10, 16):
        print(int2hex(i))
        print(hex2int(int2hex(i)))


if __name__ == "__main__":
    main()
