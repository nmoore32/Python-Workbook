##
# Determines whether a given month and day corresponds to a fixed date holiday
#

# Read month and day from user
month = input("Enter a month: ")
day = int(input("Enter a day: "))

# Determine whether the date matches a holiday and display result
if month == "January" and day == 1:
    print("New Year's Day is on January 1.")
elif month == "July" and day == 1:
    print("Canada Day is on July 1.")
elif month == "December" and day == 25:
    print("Christmas Day is on December 25")
else:
    print("There is no fixed-date holiday on that date.")