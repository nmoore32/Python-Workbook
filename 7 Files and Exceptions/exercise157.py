##
# Converts letter grade to grade points and vice-versa.
#
A = 4.0
A_MINUS = 3.7
B_PLUS = 3.3
B = 3.0
B_MINUS = 2.7
C_PLUS = 2.3
C = 2.0
C_MINUS = 1.7
D_PLUS = 1.3
D = 1.0
F = 0


# Get the first value to convert from the user
line = input("Enter a letter grade or grade point value (blank to quit): ")

while line != "":
    # First try to treat the input as a grade point value
    try:
        gp = float(line)

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

        # Display the result
        print(f"{gp} corresponds to an {grade}")

    # If the input can't be treated as a number, try treating it as a letter grade
    except ValueError:

        try:
            grade = line

            # Determines the grade points
            if grade == "A+" or grade == "A":
                gp = A
            elif grade == "A-":
                gp = A_MINUS
            elif grade == "B+":
                gp = B_PLUS
            elif grade == "B":
                gp = B
            elif grade == "B-":
                gp = B_MINUS
            elif grade == "C+":
                gp = C_PLUS
            elif grade == "C":
                gp = C
            elif grade == "C-":
                gp = C_MINUS
            elif grade == "D+":
                gp = D_PLUS
            elif grade == "D":
                gp = D
            elif grade == "F":
                gp = F

            # Display the result
            print(f"{grade} corresponds to {gp}")
        # If both conversions fail, print message indicating the input is invalid
        except:
            print("Invalid Input")

    line = input("Enter a letter grade or grade point value (blank to quit): ")
