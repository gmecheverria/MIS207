#
# Determines if water is solid, liquid, or gas at its temperature
#

# Displays the title
print("The three states of water")

# Ask for the users input
temperature = float(input("What is the temperature of the water?"))

# Prints the form of the water based on the user input
if temperature < 32:
    print("The water is ice")
elif temperature > 212:
    print("The water is steam")
else:
    print("The water is liquid")