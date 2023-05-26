#
# guessing game where the user is asked to guess the number between 1 and 10
# check to see if the user entered an int between 1 and 10,
# if not, tell the user that they entered invalid input, and prompt them again.
#

# Title
print("\nThe Guessing Game!\n")

# Gets the users input
guess = input("Enter a number between 1 and 10: ")

# The correct number to guess
correct_guess = 5

# Ask for users input again if they do not enter a number
while not guess.strip().isnumeric():
    print("invalid input")
    guess = input("Enter a number between 1 and 10: ")

# Convert the users input into integer
guess = int(guess)

# Checks if the users guess is in the correct range
while guess < 1 or guess > 10:
    print("Invalid input")
    guess = int(input("Enter a number between 1 and 10: "))

# print if the users guess is correct or not
if guess == correct_guess:
    print("You guess right!")
else:
    print("You guess wrong")