##
# Computes the surface distance between two points on Earth 
#
import math

# Read latitude and longtude of two points from user
t1 = float(input("Enter latitude of the first point: "))
g1 = float(input("Enter longitude of the first point: "))
t2 = float(input("Enter latitude of the second point: "))
g2 = float(input("Enter longitude of the second point: "))

# Convert values from degrees to radians
t1 = math.radians(t1)
g1 = math.radians(g1)
t2 = math.radians(t2)
g2 = math.radians(g2)

# Calculate distance in kilometers between points
distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1-g2))

# Display the result
print("The distance between these two points is", "%.3f" % distance, "km")
