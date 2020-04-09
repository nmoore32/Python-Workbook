##
# Program that categorizes electromagnetic radiation based on frequency
#

# Define constants that represent maximum frequency for each category
RADIO_WAVE = 3e9
MICROWAVE = 3e12
INFRARED = 4.3e14
VISIBLE = 7.5e14
ULTRAVIOLET = 3e17
XRAY = 3e19

# Read frequency from user
freq = float(input("Enter frequency in Hz: "))

# Categorize the frequency
if freq < RADIO_WAVE:
    category = "radio wave"
elif freq < MICROWAVE:
    category = "microwave"
elif freq < INFRARED:
    category = "infrared wave"
elif freq < VISIBLE:
    category = "visible wave"
elif freq < ULTRAVIOLET:
    category = "ultraviolet wave"
elif freq < XRAY:
    category = "x-ray"
else:
    category = "gamma ray"

print(f"\nElectromagnetic radiation at that frequency is a {category}.")
