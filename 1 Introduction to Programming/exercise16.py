##
# Computes the area of a circle and volume of a sphere of radius r
#

import math

# Read radius from user
r = float(input("Enter a radius: "))

#Calculate and display area
print("The area of a circle of radius", r, "is", "%.4f" % (math.pi * (r ** 2)))

# Caculate and display volume
print("The volume of a sphere of radius", r, "is", "%.4f" % ((4 / 3) * (math.pi * (r ** 3))))
