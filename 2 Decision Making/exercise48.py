##
# Determine zodiac sign given month and day
#

# Read month and day from user
month = input("Enter a month: ")
day = int(input("Enter a day: "))

# Determine the zodiac sign
if (month == "December" and day >= 22) or (month == "January" and day <= 19):
    zodiac = "Capricorn"
elif (month == "January" and day >= 20) or (month == "February" and day <= 18):
    zodiac = "Aquarius"
elif (month == "February" and day >= 19) or (month == "March" and day <= 20):
    zodiac = "Pisces"
elif (month == "March" and day >= 21) or (month == "April" and day <= 19):
    zodiac = "Aries"
elif (month == "April" and day >= 20) or (month == "May" and day <= 20):
    zodiac = "Taurus"
elif (month == "May" and day >= 21) or (month == "June" and day <= 20):
    zodiac = "Gemini"
elif (month == "June" and day >= 21) or (month == "July" and day <= 22):
    zodiac = "Cancer"
elif (month == "July" and day >= 23) or (month == "August" and day <= 22):
    zodiac = "Leo"
elif (month == "August" and day >= 23) or (month == "September" and day <= 22):
    zodiac = "Virgo"
elif (month == "September" and day >= 23) or (month == "October" and day <= 22):
    zodiac = "Libra"
elif (month == "October" and day >= 23) or (month == "November" and day <= 21):
    zodiac = "Scorpio"
elif (month == "November" and day >= 22) or (month == "December" and day <= 21):
    zodiac = "Sagttarious"

# Display output
print(month, day, "is in " + zodiac + ".")
