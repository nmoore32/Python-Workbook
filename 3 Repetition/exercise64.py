##
# Generates a table of original prices along with a discounted value
#
DISCOUNT_RATE = 0.6

# Initialize variable for price of first item
price = 4.95

# For loop to loop over each price to discount
for i in range(0, 5):
    print(f"\nOriginal price: {price:.2f}")
    discount_amount = price * DISCOUNT_RATE
    print(f"Discount amount: {discount_amount:.2f}")
    total_amount = price - discount_amount
    print(f"Total: {total_amount:.2f}")
    price += 5

