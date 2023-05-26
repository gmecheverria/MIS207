#
# Create an test a function called input_float that accepts a prompt string,
# and uses the given prompt string to ask the user for a floating point value.
# The function should return the floating point value enter.
# If the user does not enter a valid floating point value,
# print an error to the screen and ask them again.
# (NOTE: This is all done inside the function).
#

def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Invalid Input. Please try again.")
    return None

value = input_float("Enter a floating point value: ")
print(f"You entered the floating point value {value}")
