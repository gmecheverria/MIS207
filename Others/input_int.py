def input_int(prompt):
    done = False
    while not done:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please try again.")
    return None # should never get here

some_int = input_int("Please enter an Integer: ")
print(f"You entered the integer {some_int}.")
