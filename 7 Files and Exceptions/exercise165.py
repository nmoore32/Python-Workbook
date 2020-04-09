##
# Display the boys' and girls' name that was given to the most babies in a given time period.
#

# Read the first and last years from the user
try:
    first_year = int(input("Enter an initial year: "))
    last_year = int(input("Enter a final year: "))
except:
    print("Invalid input. Quitting...")
    quit()

if first_year < 1900 or first_year > 2012 or last_year < 1900 or last_year > 2012:
    print("Invalid range. Quitting...")
    quit()

# Create dictionaries to store names and the number of babies given that name
boys = {}
girls = {}

for year in range(first_year, last_year + 1):
    girl_fname = f"BabyNames/{year}_GirlsNames.txt"
    boys_fname = f"BabyNames/{year}_BoysNames.txt"

    # Add all the girls names along with the numbers of babies given that name to dictionary
    inf = open(girl_fname)
    for line in inf:
        parts = line.split()
        name = parts[0]
        if name not in girls:
            girls[name] = int(parts[1])
        else:
            girls[name] += int(parts[1])
    inf.close()

    # Add all the boys names along with the numbers of babies given that name to dictionary
    inf = open(boys_fname)
    for line in inf:
        parts = line.split()
        name = parts[0]
        if name not in boys:
            boys[name] = int(parts[1])
        else:
            boys[name] += int(parts[1])
    inf.close()

max_boys = max(boys.values())
max_girls = max(girls.values())

print("The most common boys name(s) in the period is: ")
for name in boys:
    if boys[name] == max_boys:
        print(f"{name} with {boys[name]} instances.")

print("The most common girls name(s) in that period is: ")
for name in girls:
    if girls[name] == max_girls:
        print(f"{name} with {girls[name]} instances.")
