##
# Compute area of triangle from the lengths of its sides
#
import math

# Read side lengths from user
s1 = float(input("Enter length of side 1: "))
s2 = float(input("Enter length of side 2: "))
s3 = float(input("Enter length of side 3: "))
s = (s1 + s2 + s3) / 2

# Calculate area of triangle using Heron's formula
a = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))

# Display area
print("The area of the triangle is", "%.3f" % a)
