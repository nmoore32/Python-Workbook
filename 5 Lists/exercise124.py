##
# Reads a number of (x, y) coordinates from user and displays the equation
# for the line of best fit.
#

# Read (x, y) coordinates from user until they enter a blank line
x_coords = []
y_coords = []
x_coord = input("Enter an x coordinate (blank to quit): ")
while x_coord != "":
    x_coords.append(float(x_coord))
    y_coord = float(input("Enter a y coordinate: "))
    y_coords.append(y_coord)
    x_coord = input("Enter an x coordinate (blank to quit): ")

# Calculate the terms needed to determine the slope of the line of best fit
# Calculate the sum over xy.
sum_xy = 0
for i in range(len(x_coords)):
    sum_xy += (x_coords[i] * y_coords[i])

# Calculate the sum of the x coordinates and y coordinates
sum_x = 0
sum_y = 0
for i in range(len(x_coords)):
    sum_x += x_coords[i]
    sum_y += y_coords[i]

# calculate the sum of the squares of the x coordinates
sum_x2 = 0
for x in x_coords:
    sum_x2 += x ** 2

# Calculate the slope of the line of best fit
m = (sum_xy - sum_x * sum_y / len(x_coords)) / \
    (sum_x2 - ((sum_x) ** 2) / len(x_coords))

# Calculate the y-intercept of the line of best fit
b = sum_y / len(y_coords) - m * sum_x / len(x_coords)

# Print the line of best fit
print(f"y = {m:.2f}x + {b:.2f}")
