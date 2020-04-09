##
# Calculate volume of cylinder given radius and height.
#
import math

# Read radius and height from user
r = float(input("Enter radius: "))
h = float(input("Enter height: "))

# Calculate volume
v = math.pi * (r ** 2) * h

# Display volume
print("The volume of the cylinder is", "%.1f" % v)
