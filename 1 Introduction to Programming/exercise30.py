##
# Converts a temperature from Celsius to Fahrenheit and Kelvin
#

# Read temperature from user
temp = float(input("Enter a temperature in Celsius: "))

# Calculate temperature in Fahrenheit
temp_f = temp * (9 / 5) + 32

# Calculate temperature in Kelvin
temp_k = temp + 273.15

# Display result
print(temp, "degrees Celsius is '%0.2f' degrees Fahrenheit and '%0.2f' \
       degrees Kelvin" % (temp_f, temp_k)) 