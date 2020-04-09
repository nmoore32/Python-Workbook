##
# Displays any popular gender neutral names from a given year
#

# Ask the user to enter a year
try:
    year = int(input("Enter a year from 1900 to 2012: "))
except:
    print("Invalid input. Quiting...")
    quit()

# If the year isn't in the acceptable range, provide an error message and quit
if year < 1900 or year > 2012:
    print("Year not in range. Quiting...")
    quit()

girl_fname = f"BabyNames/{year}_GirlsNames.txt"
boy_fname = f"BabyNames/{year}_BoysNames.txt"

# Create lists to store the names for the given year
girls = []
boys = []

# Get the girls names
inf = open(girl_fname)
for line in inf:
    parts = line.split()
    name = parts[0]
    girls.append(name)
inf.close()

# Get the boys names
inf = open(boy_fname)
for line in inf:
    parts = line.split()
    name = parts[0]
    boys.append(name)

# Create a list of names that appear in both lists
gender_neutral = []
for name in girls:
    if name in boys:
        gender_neutral.append(name)

# Display the results
if gender_neutral == []:
    print("There were no gender neutral names that year.")
else:
    print("The gender neutral names that year were:")
    for name in gender_neutral:
        print(name)
