####################################################################################
# Program: Sort-of-crap; a simulation of the popular casino game called 'craps'
#
#
import random

print("\n########################################")
print("## Welcome to the 'Sort-Of-Krap' game ##")
print("########################################\n")
print("\nIn this game you start with $100.00 in the pot. You can bet any amount that you have in the pot.")
print("\nIf win your bet if your total roll is a  2,3, 11 or 12. If you roll any other total, you lose your bet.")

pot = 100.00 # start with $100

done = False
while not done:
    bet = input(f"\n\nYou currently have ${pot:,.2f} in the pot. What is your bet (enter C to cash out)? ").strip()
    if bet.upper() == 'C':
        done = True
    else:
        bet = float(bet)
        if bet <= pot:
            # roll dice
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            dice = die1 + die2
            print(f"You rolled a {die1} and {die2} for a total of {dice}.")

            if dice == 2 or dice == 3 or dice == 11 or dice == 12:
                pot += bet
                print(f"Congratulations. You won ${bet:,.2f}")
            else:
                pot -= bet
                print(f"You did not win. You lost  ${bet:,.2f}")
        else:
            print(f"You only have ${pot:,.2f} to bet. Please enter a valid bet.")

print(f"\n\nYou've walked away with ${pot:,.2f}. We hope to see you back soon. Have a nice day!")


"""
So what are the odd's of winning this game? To answer this, we need to think about all the combination of rolling
two dice. 

When we write out every combination, we find the following:

(1,1)	(1,2)	(1,3)	(1,4)	(1,5)	(1,6)
(2,1)	(2,2)	(2,3)	(2,4)	(2,5)	(2,6)
(3,1)	(3,2)	(3,3)	(3,4)	(3,5)	(3,6)
(4,1)	(4,2)	(4,3)	(4,4)	(4,5)	(4,6)
(5,1)	(5,2)	(5,3)	(5,4)	(5,5)	(5,6)
(6,1)	(6,2)	(6,3)	(6,4)	(6,5)	(6,6)
 
If we count these, we find that there are 36 possible combinations.

Now, how many of these total 2? 
ans: Only (1,1) totals 2, therefore there is only one possible roll that produces 2.

Now, how many of these total 3? 
ans: (1,2) and (2,1) total 3, therefore there are two possible rolls that produces 3.

Now, how many of these total 2? 
ans: (5,6) and (6,5) total 11, therefore there are two possible rolls that produces 11.

Now, how many of these total 2? 
ans: Only (6,6) totals 12, therefore there is only one possible roll that produces 12.

Therefore, the odds of rolling either a 2,3,11 or 12 are:
1/36 + 2/36 + 2/36 + 1/36 = 6/36 = 1/6 = 16.67%.

So, 16.67% percent of the time you win your bet, and 83.33% of the time the house gets your bet.

Is this a fair game?  

"""