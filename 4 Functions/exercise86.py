def taxi_fare(kilometers):
    """ This function computes taxi fare from distance traveled in kilometers. """
    BASE_FARE = 4.00
    INCREMENT_PER_140 = 0.25

    fare = BASE_FARE + (kilometers * (0.25 / 0.140))
    return fare


def main():

    distance = float(input("Enter a distance in kilometers: "))

    print(f"The fare will be {taxi_fare(distance):.2f}")


main()
