#
# A program that simulates the outcome of a user
# print how much the user has in the pot at the end of the simulation
# writes a comment at the end of the program, if I expected those results
#

# to be able to use randint
import random

# what the simulation is about
print("\nSimulates the outcome of a user who begins with $10,000 in the pot and bets $1 on 10,000 plays")

# initial numbers
POT = 10000
PLAY = 10000
BET = 1

for i in range(PLAY + 1):
    if BET <= POT:
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        dice = die1 + die2

        if dice == 2 or dice == 3 or dice == 11 or dice == 12:
            POT += BET
        else:
            POT -= BET

# prints the total amount left in the pot
print(f"\nAt the end, you walk away with ${POT:,.2f}")

# Expected a lower number but it is not surprising
