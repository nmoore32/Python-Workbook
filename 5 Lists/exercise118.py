##
# Reports whether a string entered by the user is a word by word palindrome.
#
from exercise117 import getWords

## Determines whether a string is a word by word palindrome.
# @param string the string to test
# @return True if the string is a word by word palindrome, False otherwise
def isWordPalindrome(string):
    # Convert the string to a list of words with punctuation removed
    words = getWords(string)

    # Check if the list of words is not a palindrome, if not return False
    for i in range(len(words) // 2):
        if words[i].lower() != words[-1 - i].lower():
            return False
    return True


# Reports whether a string entered by the user a word by word palindrome
def main():
    line = input("Enter a string: ")
    if isWordPalindrome(line):
        print(f'"{line}" is a word-by-word palindrome.')
    else:
        print(f'{line}" is not a word-by-word palindrome.')


if __name__ == "__main__":
    main()
