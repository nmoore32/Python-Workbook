##
# Reads date from user and computes its immediate successor.
#

# Read date from user
print("\nEnter a date in yyyy-mm-dd format.")
day = int(input("Enter a day: "))
month = int(input("Enter a month: "))
year = int(input("Enter a year: "))
date = f"{year}-{month}-{day}"

# Determine if the year is a leap year
if year % 400 == 0:
    isLeapYear = True
elif year % 100 == 0:
    isLeapYear = False
elif year % 4 == 0:
    isLeapYear = True
else:
    isLeapYear = False

# Determine the successor date
if day < 28:
    day += 1
elif (day == 28) and (isLeapYear):
    day += 1
elif day == 28 and month == 2:
    day = 1
    month += 1
elif day == 28 and month != 2:
    day += 1
elif day == 29 and month == 2:
    day = 1
    month += 1
elif day < 30:
    day += 1
elif (day == 30) and (month == (4 or 6 or 9 or 11)):
    day = 1
    month += 1
elif (day == 30) and (month != (4 or 6 or 9 or 11)):
    day += 1
elif (day == 31) and month != 12:
    day = 1
    month += 1
else:
    day = 1
    month = 1
    year += 1

print(f"The next date after {date} is {year}-{month}-{day}")
