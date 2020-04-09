##
# Provides reference noises for Decibel levels
#
JACKHAMMER = "Jackhammer = 130 dB"
GAS_LAWNMOWER = "Gas Lawnmower = 106 dB"
ALARM_CLOCK = "Alarm Clock = 70 dB"
QUIET_ROOM = "Quiet Room = 40 dB"

# Read Decibel level from user
dec = int(input("Enter a number of Decibels: "))

# Determine reference noises to provide and display result
if dec > 130:
    print("That is very loud!")
elif dec == 130:
    print(JACKHAMMER)
elif dec < 130 and dec > 106:
    print(JACKHAMMER)
    print(GAS_LAWNMOWER)
elif dec == 106:
    print(GAS_LAWNMOWER)
elif dec < 106 and dec > 70:
    print(GAS_LAWNMOWER)
    print(ALARM_CLOCK)
elif dec == 70:
    print(ALARM_CLOCK)
elif dec < 70 and dec > 40:
    print(ALARM_CLOCK)
    print(QUIET_ROOM)
elif dec == 40:
    print(QUIET_ROOM)
else:
    print("That is very quiet!")