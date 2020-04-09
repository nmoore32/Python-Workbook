##
# Given a grade point value returns the corresponding letter grade
#

# Read value from user
gp = float(input("Enter a grade point value: "))

# Determine the corresponding letter grade
if gp >= 4.0:
    grade = "A or A+"
elif gp < 4.0 and gp >= 3.85:
    grade = "A"
elif gp < 3.85 and gp >= 3.50:
    grade = "A-"
elif gp < 3.50 and gp >= 3.15:
    grade = "B+"
elif gp < 3.15 and gp >= 2.85:
    grade = "B"
elif gp < 2.85 and gp >= 2.50:
    grade = "B-"
elif gp < 2.50 and gp >= 2.15:
    grade = "C+"
elif gp < 2.15 and gp >= 1.85:
    grade = "C"
elif gp < 1.85 and gp >= 1.50:
    grade = "C-"
elif gp < 1.50 and gp >= 1.15:
    grade = "D+"
elif gp < 1.15 and gp >= 0.50:
    grade = "D"
elif gp > 0 and gp < 0.50:
    grade = "F"
else:
    grade = ""

if grade:
    print(f"\n{gp}: {grade}")
else:
    print("\nInvalid number of grade points entered.")
