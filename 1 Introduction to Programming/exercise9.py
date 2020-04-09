##
# Calculate savings value after one to three years of annual interest
#
INTEREST_RATE = 0.04

# Read initial account balance from user
savings = float(input("Enter savings account balance: "))

# Caculate new balance after one, two, and three years
savings1 = savings + savings * 0.04
savings2 = savings1 + savings1 * 0.04
savings3 = savings2 + savings2 * 0.04

# Display result
print("Balance after 1 year: $" + "%.2f" % savings1)
print("Balance after 2 years: $" + "%.2f" % savings2)
print("Balance after 3 years: $" + "%.2f" % savings3)
