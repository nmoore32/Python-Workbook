##
# Converts time interval into seconds
#
S_PER_D = 86400
S_PER_H = 3600
S_PER_M = 60

# Read input from user
d = float(input("Enter number of days: "))
h = float(input("Enter number of hours: "))
m = float(input("Enter number of minutes: "))
s = float(input("Enter number of seconds: "))

# Calculate number of seconds
seconds = d * S_PER_D + h * S_PER_H + m * S_PER_M + s

# Display number of seconds
print(d, "days,", h, "hours,", m, "minutes, and", s, "seconds is", seconds, "seconds.")
