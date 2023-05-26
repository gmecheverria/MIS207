#
# Create a number guessing game.
# The player is allowed up to 7 chances to guess a number between 1 and 100.
# For each incorrect guess, the player will receive feedback
# on if their guess was greater than or less than the number the computer was thinking.
# If the user enters a value outside this range, then they wish to exit the program early.
#

# import to use the randint
import random

# title
print("The Guessing Game!\nYou have 7 chances to guess the correct number")

done = False
count = 0
correct_answer = random.randint(1, 100)  # generates a random correct answer

while True:
    try:
        while not done:
            guess_num = int(input("Guess a number between 1 and 100: "))
            # gives the user a way to exit the game
            if guess_num < 1 or guess_num > 100:
                exit_program = input("Do you wish to exit the program (Y or N)? ")
                if exit_program.lower() == "y":
                    print("Good Bye!")
                    done = True
            # gives the feedback to users to get them closer to the correct answer
            elif guess_num < correct_answer:
                print("Your guess is to low")
            elif guess_num > correct_answer:
                print("Your guess is to high")
            else:
                print("You guess right!\nGood Game!")
                done = True
            count += 1  # counts how many times the user guesses
            if count == 7:
                print(f"You are out of chances the correct answer is {correct_answer}")
                done = True

    except ValueError:
        print("Invalid Input. Please enter a number.")