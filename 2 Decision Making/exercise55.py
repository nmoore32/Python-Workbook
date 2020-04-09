##
# Reads a wavelength in the visible spectrum and returns a color
#

# Read wavelength from user
wavelength = float(input("Enter a wavelenth in nm: "))

# Determine the color
if 380 <= wavelength < 450:
    color = "violet"
elif 450 <= wavelength < 495:
    color = "blue"
elif 495 <= wavelength < 570:
    color = "green"
elif 570 <= wavelength < 590:
    color = "yellow"
elif 590 <= wavelength < 620:
    color = "orange"
elif 620 <= wavelength <= 750:
    color = "red"
else:
    color = ""

# Print the result
if color == "":
    print(f"\nLight of {wavelength:.0f} nm is outside the visible spectrum.")
else:
    print(f"\nLight of {wavelength:.0f} nm is {color}.")
