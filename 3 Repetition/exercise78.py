##
# Collatz Conjecture sequence
#

# Read positive integer from user
last_term = int(input("Enter a positive integer: "))
print(last_term)

# Calculate the next term in the sequence
while last_term != 1:
    if last_term % 2 == 0:
        last_term = last_term // 2
    else:
        last_term = last_term * 3 + 1
    print(last_term)
