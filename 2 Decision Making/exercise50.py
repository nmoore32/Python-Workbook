##
# Given a magnitude on the Richter scale, returns a descriptor
#

# Get magnitude from user
mag = float(input("Enter a magnitude: "))

# Determine the result
desc = ""

if mag < 2.0:
    desc = "micro"
elif 2.0 <= mag < 3.0:
    desc = "very minor"
elif 3.0 <= mag < 4.0:
    desc = "minor"
elif 4.0 <= mag < 5.0:
    desc = "light"
elif 5.0 <= mag < 6.0:
    desc = "moderate"
elif 6.0 <= mag < 7.0:
    desc = "strong"
elif 7.0 <= mag < 8.0:
    desc = "major"
elif 8.0 <= mag < 10.0:
    desc = "great"
else:
    desc = "meteoric"

# Print the result
print(f"\n{mag} on the Richter is a {desc} earthquake.")
