##
# Program displays a temperature conversion table for Celsius and Fahrenheit
#

# Initial temperature, in Celsius to include
temp_C = 0

for i in range(11):
    temp_F = (temp_C * (9 / 5)) + 32
    print(f"{temp_C} Celsius is {temp_F:.0f} Fahrenheit")
    temp_C += 10

