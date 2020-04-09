##
# Compute BMI
#

# Read height and weight from user
height = float(input("Enter your height in inches: "))
weight = float(input("Enter your weight in pounds: "))

# Calculate BMI
bmi = weight * 703 / (height ** 2)

# Display result
print("Your BMI is", "%.1f" % bmi)
