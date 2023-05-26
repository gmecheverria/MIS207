#
#  Boolean Expressions
#

# Gets the users input
number1 = int(input("Enter your first number:"))
number2 = int(input("Enter your second number:"))

# Displays whether both the number is odd, even, or neither
if number1 % 2 == 0 and number2 % 2 == 0:
    print("The numbers are even")
elif number1 % 2 != 0 and number2 % 2 != 0:
    print("The numbers are odd")
else:
    print("Both the numbers are not odd or even")

myAge = 19  # Initial age used to compare to the users numbers

age = number1 + number2  # Adds the users numbers together

# Prints if the users numbers added together are greater, less than, or equal to the initial age
if age > myAge:
    print("You are older than me")
elif age < myAge:
    print("You are younger than me")
else:
    print("We are the same age")

