############################################################
# MIS207 - Prompt until Match Algorithm
# Author: Dr. Tim Smith
# Description:
#   The following code demonstrates a while loop pattern of re-asking user for input
#   is the input is out of range.
#


########################################################
# get user input and keep track of count and total

valid = False
while not valid:  # keep going until user provides something valid input
    value = int(input("Enter a positive integer value less than 100 (anything else to quite): "))
    if 0 <= value < 100:
        valid = True
    else:
        print("Invalid input. Please try again.")

########################################################
# print results

print(f"You entered {value}.")
