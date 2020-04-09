##
# Determine the prime factorization of an integer
#

# Read an integer from user
n = int(input("Enter an integer (2 or greater): "))
if n < 2:
    print("Please enter an integer of 2 or greater!")

print(f"The prime factors of {n} are:")

factor = 2
while factor <= n:
    if n % factor == 0:
        print(factor)
        n = n // factor
    else:
        factor += 1
