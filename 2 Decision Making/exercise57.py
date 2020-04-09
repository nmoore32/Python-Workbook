##
# Calculates a phone bill given a number of minutes and text messages
#
PLAN_COST = 15.00
ADDITIONAL_MINUTE = 0.25
ADDITIONAL_TEXT = 0.15
EMERGENCY_CHARGE = 0.44
TAX_RATE = 0.05

# Get numner of minutes and number of text messages from user
minutes = int(input("\nEnter number of minutes: "))
texts = int(input("Enter number of texts: "))

# Determine additional charges
minutes_cost = 0
texts_cost = 0

if minutes > 50:
    additional_minutes = minutes - 50
    minutes_cost = additional_minutes * ADDITIONAL_MINUTE
if texts > 50:
    additional_texts = texts - 50
    texts_cost = additional_texts * ADDITIONAL_TEXT

# Determine the total cost
total_cost = PLAN_COST + minutes_cost + texts_cost + EMERGENCY_CHARGE
total_cost = total_cost + (total_cost * TAX_RATE)

# Display the results
print(f"\nBase charge: {PLAN_COST:.2f}")
if minutes_cost:
    print(f"Additional minutes: {minutes_cost:.2f}")
if texts_cost:
    print(f"Additional texts: {texts_cost:.2f}")
print(f"911 support: {EMERGENCY_CHARGE:.2f}")
print(f"\nTotal: {total_cost:.2f}")
