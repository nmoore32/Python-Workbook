##
# Reads baby names from files and makes lists of all the distinct boys and girls names
#

girls = []
boys = []

for year in range(1900, 2013):
    girl_fname = f"BabyNames/{year}_GirlsNames.txt"
    boy_fname = f"BabyNames/{year}_BoysNames.txt"

    inf = open(girl_fname)
    for line in inf:
        parts = line.split()
        name = parts[0]
        if name not in girls:
            girls.append(name)
    inf.close()

    inf = open(boy_fname)
    for line in inf:
        parts = line.split()
        name = parts[0]
        if name not in boys:
            boys.append(name)
    inf.close()

print(sorted(boys))
print(sorted(girls))
