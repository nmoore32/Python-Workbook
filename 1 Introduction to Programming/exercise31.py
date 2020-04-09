##
# Converts pressure from kilopascals to pounds per square inch,
# millimeters of mercury, and atmospheres.
#
KPA_TO_LB_PER_INCH = 1 / 6.89476
KPA_TO_ML_MERC = 7.5
KPA_TO_ATM = 1 / 101.325

# Read pressure from user
p = float(input("Enter pressure in kilopascals: "))

# Calculate results
lb = p * KPA_TO_LB_PER_INCH
ml = p * KPA_TO_ML_MERC
atm = p * KPA_TO_ATM

# Display results
print("%0.3f" % lb, "pounds per inch")
print("%0.3f" % ml, "milliters of mercury")
print("%0.3f" % atm, "atmospheres")