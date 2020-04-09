##
# Provides success approximations of pie
#

# Print the first approximation
pi = 3
print(pi)

# Use for loop to print successive approximations
for i in range(1, 15):
    if i % 2 != 0:
        pi += 4 / (2 * i * (2 * i + 1) * (2 * i + 2))
    else:
        pi -= 4 / (2 * i * (2 * i + 1) * (2 * i + 2))
    print(pi)
