#
# Create a guess my number game that asks a user to guess the number (between 1 and 10)
# checks to see if the user guessed 7
#

# Title
print("\nWelcome to guess my number game!\n")

# gets the users input
guess_number = int(input("Pick a whole number between 1-10: "))

# the number the users have to guess
correct_number = 7

# print if the user guess correctly or not
if guess_number in range(0, 10):
#if guess_number >= 1 and guess_number <= 10:
    if guess_number == correct_number:
        print("Congratulations you guess correctly!")
    elif guess_number > correct_number:
        print("Incorrect your guess was to high")
    else:
        print("Incorrect your guess was to low")
else:
    print("Invalid Input")

# goodbye
print("\nGood game!")
