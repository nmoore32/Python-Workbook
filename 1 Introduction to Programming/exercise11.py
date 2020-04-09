##
# Converts fuel efficiency from American units (miles-per-gallon)
# to Canadian units (liters-per-hundred-kilometers)
#

# Read fuel efficiency in American units from user
MPG = float(input("Enter fuel efficiency in miles-per-gallon: "))

# Computes fuel efficiency in Canadian units
liters_per_100 = 235.215 / MPG

# Display result
print("Fuel efficiency is", "%.3f" % (liters_per_100), "L/100 km")
