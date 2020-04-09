##
# Given a postal code indicates the associated province and whether the address is rural
# or urban. The first character indicates the province. The second character indicates
# whether the address is rural (0), or urban (!0).
#
POS_TO_PRO = {"A": "Newfoundland", "B": "Nova Scotia", "C": "Prince Edward Island",
              "E": "New Brunswick", "G": "Quebec", "H": "Quebec", "J": "Quebec", "K": "Ontario",
              "L": "Ontario", "M": "Ontario", "N": "Ontario", "P": "Ontario", "R": "Manitoba",
              "S": "Saskatchewan", "T": "Alberta", "V": "British Columba",
              "X": "Nunavut or Northwest Territories", "Y": "Yukon"}

postal = (input("Enter a postal code: ")).upper()
if (postal[0] not in POS_TO_PRO) or not ("0" <= postal[1] <= "9"):
    print("That is not a valid postal code.")
else:
    classificiation = ""
    if postal[1] == "0":
        classification = " rural"
    else:
        classification = "n urban"
    print(
        f"That postal code is corresponds to a{classification} address in",
        f"{POS_TO_PRO[postal[0]]}.")
