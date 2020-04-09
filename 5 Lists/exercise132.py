##
# Evaluates a postfix expression and displays the result
#
from exercise96 import isInteger
from exercise97 import precedence
from exercise129 import tokenList
from exercise130 import identifyUnary
from exercise131 import infix2postfix

OPERATORS = ["*", "/", "^", "+", "-"]

# Evaluates a postfix expression
# @param exp the expression to evaluate
# @returm the value of the expression


def evaluatePostfix(exp):
    values = []

    for token in exp:
        if isInteger(token):
            values.append(int(token))
        elif token == "u-":
            values.append(-values.pop())
        elif token in OPERATORS:
            right = values.pop()
            left = values.pop()
            if token == "+":
                values.append(left + right)
            elif token == "-":
                values.append(left - right)
            elif token == "*":
                values.append(left * right)
            elif token == "/":
                values.append(left / right)
    return values[0]

# Demonstrates evaluatePostfix by evaluating postfix expressions from user


def main():
    exp = input("Enter a mathematical expression: ")
    tokens = tokenList(exp)
    print(tokens)
    marked = identifyUnary(tokens)
    print(marked)
    post = infix2postfix(marked)
    print(post)
    print(evaluatePostfix(post))


if __name__ == "__main__":
    main()
