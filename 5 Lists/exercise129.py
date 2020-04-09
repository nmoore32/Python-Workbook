##
# Tokenizes a string containing a math expression
#
OPERATORS = ["*", "/", "^", "+", "-"]
DELIMITERS = ["(", ")", "[", "]", "{", "}"]

# Convert a mathematical expression into a list of tokens
# @param s the string to tokenize
# @return a list of the tokens in s, or an empty list


def tokenList(s):
    # Remove all the spaces from s
    s = s.replace(" ", "")

    # Loop through the characters in the string adding identified tokens to the list
    tokens = []
    i = 0
    while i < len(s):
        # Handle all of the single character tokens
        if s[i] in OPERATORS or s[i] in DELIMITERS:
            tokens.append(s[i])
            i += 1
        # Handle all the numbers
        elif "0" <= s[i] <= "9":
            num = ""
            # Keep adding characters to the token as long as they're digits
            while i < len(s) and "0" <= s[i] and s[i] <= "9":
                num = num + s[i]
                i += 1
            tokens.append(num)

        # Any other character ented means the expression isn't valid.
        else:
            return []

    return tokens

# Read an expression from the user, tokenize it, and display the result


def main():
    exp = input("Enter a mathematical expression: ")
    tokens = tokenList(exp)
    print(f"The tokens are: {tokens}")


# Call the main function only if it hasn't been imported
if __name__ == "__main__":
    main()
