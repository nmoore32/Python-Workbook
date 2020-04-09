##
# Calculate number of moles of gas using the ideal gas law
#

# Ideal gas constant
R = 8.314

# Read pressure, temperature, and volume from user
p = float(input("Enter pressure in pascals: "))
t = float(input("Enter temperature in Kelvins: "))
v = float(input("Enter volume in liters: "))

# Calculate the number of moles of gas
n = (p * v) / (R * t)

#Display the result
print("There are", "%.4f" % n, "moles of gas")
