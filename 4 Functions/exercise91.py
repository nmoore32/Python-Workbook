##
# Reads a day, month, and year from the user and displays the day of the year it is.
#
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

# Determine the ordinal date
def ordinalDate(day, month, year):
    # Determine if the year is a leap year
    if year % 400 == 0:
        isLeapYear = True
    elif year % 100 == 0:
        isLeapYear = False
    elif year % 4 == 0:
        isLeapYear = True
    else:
        isLeapYear = False

    # Initialize variable to keep track of the number of days in the year
    day_of_year = 0

    # Determine the ordinal date
    if month == 1:
        return day

    # Add all the days of the previous months if month > 1
    if month > 1:
        day_of_year += DAYS_IN_JANUARY
    if month > 2:
        day_of_year += DAYS_IN_FEBRUARY
    if month > 3:
        day_of_year += DAYS_IN_MARCH
    if month > 4:
        day_of_year += DAYS_IN_APRIL
    if month > 5:
        day_of_year += DAYS_IN_MAY
    if month > 6:
        day_of_year += DAYS_IN_JUNE
    if month > 7:
        day_of_year += DAYS_IN_JULY
    if month > 8:
        day_of_year += DAYS_IN_AUGUST
    if month > 9:
        day_of_year += DAYS_IN_SEPTEMBER
    if month > 10:
        day_of_year += DAYS_IN_OCTOBER
    if month > 11:
        day_of_year += DAYS_IN_NOVEMBER

    # Add the days of the current month
    day_of_year += day

    # Add an extra day if it's a leap year and after February
    if isLeapYear and month > 2:
        day_of_year += 1

    # Return the numbers of day since the beginning of the year
    return day_of_year


# Define main function
def main():

    # Read input from user
    d = int(input("Enter the day: "))
    m = int(input("Enter the month: "))
    y = int(input("Enter the year: "))

    print(ordinalDate(d, m, y))


if __name__ == "__main__":
    main()
