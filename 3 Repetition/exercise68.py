##
# Computes GPA from a list of letter grades provided by user
#
A_PLUS = 4.0
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

# Track sum of grade points for letter grades entered and number of grades entered
sum = 0
count = 0

# Read the first letter grade from user
grade = input("Enter a letter grade (blank to quit): ")

# Read additional letter grades from user until they enter a blank line
while grade != "":

    # Add the grade points for the letter grade to sum
    if grade == "A+" or grade == "A":
        sum += A_PLUS
    elif grade == "A-":
        sum += A_MINUS
    elif grade == "B+":
        sum += B_PLUS
    elif grade == "B":
        sum += B
    elif grade == "B-":
        sum += B_MINUS
    elif grade == "C+":
        sum += C_PLUS
    elif grade == "C":
        sum += C
    elif grade == "D+":
        sum += D_PLUS
    elif grade == "D":
        sum += D

    # Increment the counter by one
    count += 1

    # Read the next letter grade
    grade = input("Enter a letter grade (blank to quit): ")

# Calculate the average
gpa = sum / count

# Display the result
print(f"Your GPA is {gpa:.2f}.")
