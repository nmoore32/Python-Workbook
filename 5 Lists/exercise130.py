##
# Differentiate between unary and binary + and - operators
#
from exercise129 import tokenList

OPERATORS = ["*", "/", "^", "+", "-"]
DELIMITERS = ["(", ")", "[", "]", "{", "}"]

# Identifies unary operators in a list of tokens replacing them with u+ or u-
# @param tokens the list of tokens to examine
# @return a new list of tokens with the unary operators, if any, indicated


def identifyUnary(tokens):
    retval = []
    # Go through each token in the list
    for i in range(len(tokens)):
        # If the first token is + or - then it's unary
        if i == 0 and (tokens[i] == "+" or tokens[i] == "-"):
            retval.append("u" + tokens[i])
        # A + or - preceded by an operator or delimeter is unary
        elif i > 0 and ((tokens[i] == "+" or tokens[i] == "-") and
                        (tokens[i - 1] in OPERATORS or tokens[i - 1] in DELIMITERS)):
            retval.append("u" + tokens[i])
        # Any other token is not unary so is just added to the result as is
        else:
            retval.append(tokens[i])

    # Return the result
    return retval

# Demonstrate that unary operators are marked correctly


def main():
    # Read expression from user, tokenize it, and print result
    exp = input("Enter a mathematical expression: ")
    tokens = tokenList(exp)
    print(f"The tokens are: {tokens}")

    # Identify the unary operators in the list of tokens
    new_tokens = identifyUnary(tokens)
    print(f"With unary operators: {new_tokens}")


if __name__ == "__main__":
    main()
