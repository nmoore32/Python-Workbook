##
# Determines what day of the week January 1st is for a given year
#

# Read year from user
year = int(input("Enter a year: "))

# Determine an integer representing the day of the week
day_of_the_week = (
    year + ((year - 1) // 4) - ((year - 1) // 100) + (year - 1) // 400
) % 7

# Convert that integer into the name of the day
if day_of_the_week == 0:
    day = "Sunday"
elif day_of_the_week == 1:
    day = "Monday"
elif day_of_the_week == 2:
    day = "Tuesday"
elif day_of_the_week == 3:
    day = "Wednesday"
elif day_of_the_week == 4:
    day = "Thursday"
elif day_of_the_week == 5:
    day = "Friday"
elif day_of_the_week == 6:
    day = "Saturday"

# Display the result
print(f"\nJanuary 1st of {year} is a {day}.")
