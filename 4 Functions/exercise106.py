##
# Displays the number of days in a month specified by the user.
#

## Determines the number of days in a given month
# @param month the month entered as an integer
# @param the year
# @return the number of days in the month
def days_in_month(month, year):
    # Determine if the year is a leap year
    if year % 400 == 0:
        isLeapYear = True
    elif year % 100 == 0:
        isLeapYear = False
    elif year % 4 == 0:
        isLeapYear = True
    else:
        isLeapYear = False

    # Determine the number of days in the month
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    if month == 2 and isLeapYear:
        return 29
    if month == 2:
        return 28
    return 31


# Displays the number of days in a month entered by user
def main():
    month = int(input("Enter a month (as an integer): "))
    year = int(input("Enter a year: "))

    print(days_in_month(month, year))


if __name__ == "__main__":
    main()

