#
# Ask the user to enter a number between 1 and 10
#

# Get users input
users_number = int(input("Enter a number between 1 and 10: "))


# Repeats if the user enters a number not between 1 and 10
while users_number < 1 or users_number > 10:
    print("Invalid input")
    users_number = int(input("Enter a number between 1 and 10: "))

