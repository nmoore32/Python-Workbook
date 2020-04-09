##
# Converts feet to inches, yards, and miles
#
IN_PER_FT = 12
YARD_PER_FT = 1/3
MILE_PER_FT = 1 / 5280

# Read value from user
feet = float(input("Enter a measurement in feet: "))

# Calculate and print results
print(feet, "feet is", "%.4f" % (feet * IN_PER_FT))
print(feet, "feet is", "%.4f" % (feet * YARD_PER_FT))
print(feet, "feet is", "%.4f" % (feet * MILE_PER_FT))
 
