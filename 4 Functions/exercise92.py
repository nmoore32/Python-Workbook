##
# Reads a day, month, and year from the user and displays the day of the year it is.
#
from exercise91 import ordinalDate

DAYS_IN_JANUARY = 31
DAYS_IN_FEBRUARY = 28
DAYS_IN_MARCH = 31
DAYS_IN_APRIL = 30
DAYS_IN_MAY = 31
DAYS_IN_JUNE = 30
DAYS_IN_JULY = 31
DAYS_IN_AUGUST = 31
DAYS_IN_SEPTEMBER = 30
DAYS_IN_OCTOBER = 31
DAYS_IN_NOVEMBER = 30
DAYS_IN_DECEMBER = 31

## Determines whether a given year is a leap year
def leapYear(year):
    # Determine if the year is a leap year
    if year % 400 == 0:
        isLeapYear = True
    elif year % 100 == 0:
        isLeapYear = False
    elif year % 4 == 0:
        isLeapYear = True
    else:
        isLeapYear = False
    return isLeapYear


## Given an ordinal date, gives the day and month of that date
# @param year the given year
# @param the ordinal day of the year
# @return day, month
def convertOrdinal(year, day):
    # Determine if the current year is a leap year
    isLeapYear = leapYear(year)

    if day <= DAYS_IN_JANUARY:
        return day, 1
    else:
        day -= DAYS_IN_JANUARY
    if day <= DAYS_IN_FEBRUARY or ((day == (DAYS_IN_FEBRUARY + 1)) and isLeapYear):
        return day, 2
    if isLeapYear:
        day -= DAYS_IN_FEBRUARY + 1
    else:
        day -= DAYS_IN_FEBRUARY
    if day <= DAYS_IN_MARCH:
        return day, 3
    else:
        day -= DAYS_IN_MARCH
    if day <= DAYS_IN_APRIL:
        return day, 4
    else:
        day -= DAYS_IN_APRIL
    if day <= DAYS_IN_MAY:
        return day, 5
    else:
        day -= DAYS_IN_MAY
    if day <= DAYS_IN_JUNE:
        return day, 6
    else:
        day -= DAYS_IN_JUNE
    if day <= DAYS_IN_JULY:
        return day, 7
    else:
        day -= DAYS_IN_JULY
    if day <= DAYS_IN_AUGUST:
        return day, 8
    else:
        day -= DAYS_IN_AUGUST
    if day <= DAYS_IN_SEPTEMBER:
        return day, 9
    else:
        day -= DAYS_IN_SEPTEMBER
    if day <= DAYS_IN_OCTOBER:
        return day, 10
    else:
        day -= DAYS_IN_OCTOBER
    if day <= DAYS_IN_NOVEMBER:
        return day, 11
    else:
        day -= DAYS_IN_NOVEMBER
        return day, 12


# Define main function
def main():

    # Read date from user
    d = int(input("Enter a day: "))
    m = int(input("Enter a month: "))
    y = int(input("Enter a year: "))

    # Determine if the year is a leap year
    isLeapYear = leapYear(y)

    # Determine the ordinal date and add 90 days
    days = ordinalDate(d, m, y)
    days += 90

    # If the new date is in the following year, determine how many days
    # into the year and increment y by 1
    if isLeapYear and days > 366:
        days = days % 366
        y += 1
    elif days > 365:
        days = days % 365
        y += 1

    # Convert the new ordinal date back into a regular date
    new_date = convertOrdinal(y, days)
    days = new_date[0]
    month = new_date[1]

    # Print out the new date
    print(f"90 days from the entered date will be: {y}-{month}-{days}")


if __name__ == "__main__":
    main()
