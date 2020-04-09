##
# Determines the month and day of Easter given a year
#

# Get year from user
year = int(input("Enter a year: "))

# Anonymous Gregorian Computus algorithm
a = year % 19
b = year // 100
c = year % 100
d = b // 4
e = b % 4
f = (b + 8) // 25
g = (b - f + 1) // 3
h = (19 * a + b - d - g + 15) % 30
i = c // 4
k = c % 4
l = (32 + 2 * e + 2 * i - h - k) % 7
m = (a + 11 * h + 22 * l) // 451
month = (h + l - 7 * m + 114) // 31
day = 1 + (h + l - 7 * m + 114) % 31

# Determine if Easter is in March or April that year
if month == 3:
    month = "March"
else:
    month = "April"

# Display result
print("That year Easter is", month, "%d, %d." % (day, year))
