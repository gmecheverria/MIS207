#
# This program computes taxes following a schedule.
#

# Constant variables for the tax rates
RATE1 = 0.10
RATE2 = 0.15
RATE3 = 0.25

# Title
print("Computes Taxes")

# Gets the user's marital status and income
income = float(input("Enter your income:"))
maritalStatus = input("Enter s for single and m for married:")

# Calculates taxes due
if maritalStatus.lower() == "s":
    if income <= 9000:
        tax = RATE1 * income
    elif income <= 32000:
        tax = (900 + RATE2) * (income - 9000)
    else:
        tax = (4350 + RATE3) * (income - 32000)
else:
    if income <= 18000:
        tax = RATE1 * income
    elif income <= 64000:
        tax = (1800 + RATE2) * (income - 18000)
    else:
        tax = (8700 + RATE3) * (income - 64000)

# Prints the results
print(f"The tax is {tax:,.2f}")
