##
# Converts a mathematical expression from infix to postfix form
#
from exercise96 import isInteger
from exercise97 import precedence
from exercise129 import tokenList
from exercise130 import identifyUnary

OPERATORS = ["*", "/", "^", "+", "-", "u+", "u-"]
OPEN_DELIMITERS = ["(", "[", "{"]
CLOSE_DELIMITERS = [")", "]", "}"]

# Convert a mathematical expression from infix to postfix form
# @param exp the expression to convert
# @return a list of operators in the proper postfix order


def infix2postfix(exp):
    operators = []
    postfix = []

    # Loop through each token in the expression
    for token in exp:
        # If the token is an integer, append it to postfix
        if isInteger(token):
            postfix.append(token)
        # If the token is an operator
        elif token in OPERATORS:
            # Determine whether the current token or the last operator in operators has
            # precedence and append them to postfix in the correct order
            while (operators != []) and (operators[-1] not in OPEN_DELIMITERS) \
                    and (precedence(token) < precedence(operators[-1])):
                postfix.append(operators.pop())
            operators.append(token)
        # If the token is an open delimeter, append it to operators
        elif token in OPEN_DELIMITERS:
            operators.append(token)
        # If the token is a closing delimeter, append any operators in operators[]
        # back to the corresponding open delimiter
        elif token in CLOSE_DELIMITERS:
            while operators[-1] not in OPEN_DELIMITERS:
                postfix.append(operators.pop())
            # Remove the opening delimiter from operators. Postfix doesn't use delimeters.
            operators.pop()

    # After going through all the tokens append any remaining operators in operators[]
    while operators:
        postfix.append(operators.pop())

    return postfix

# Demonstrate the infix to postfix function on user input


def main():
    line = input("Enter a mathematical expression: ")
    tokens = tokenList(line)
    marked = identifyUnary(tokens)
    new_exp = infix2postfix(marked)
    print(new_exp)


if __name__ == "__main__":
    main()
