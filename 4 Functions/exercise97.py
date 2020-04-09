##
# Displays the precedence of an operator entered by the user
#
OPERATORS = ["*", "/", "^", "+", "-", "u+", "u-", "**", ]

# Determines the precedence of an operator
# @param s a string containing the operator to test
# @return an integer indicating precedence, higher value means higher precedence


def precedence(s):
    # Display an error message if the given input is not an operator
    if s not in OPERATORS:
        return "That is not an operator."
    if s == "+" or s == "-":
        return 1
    if s == "*" or s == "/":
        return 2
# Added support for unary operators and increased rank for ** and ^ by 1
    if s == "u+" or s == "u-":
        return 3
    if s == "**" or s == "^":
        return 4


# Demonstrate the precedence function
def main():
    # Read operator from user
    s = input("Enter an operator: ")
    print(precedence(s))


if __name__ == "__main__":
    main()
