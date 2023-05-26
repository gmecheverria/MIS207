#
# Calculates the discount a price of a purchase on Kilobyte Day
#

# Title
print("Calculates the price of computer accessory on Kilobyte Day")

# Gets the user input
initialTotal = float(input("What the total of your purchase?"))

# Computes which discount the user receives
if initialTotal >= 128:
    print("You receive a 16% discount")
    total = 0.16 * initialTotal
    total = initialTotal - total
else:
    print("You receive a 8% discount")
    total = 0.08 * initialTotal
    total = initialTotal - total

# prints the result
print(f"Your total is ${total:,.2f}")
