def shipping_rate(number_of_items):
    """Calculates shipping rate given number of items."""
    BASE_RATE = 10.95
    ADDITIONAL_ITEM = 2.95

    rate = BASE_RATE + ADDITIONAL_ITEM * (number_of_items - 1)
    return rate


def main():

    number_of_items = int(input("Enter the number of items: "))

    shipping_charge = shipping_rate(number_of_items)

    print(f"The shipping charge is {shipping_charge:.2f}.")


main()
