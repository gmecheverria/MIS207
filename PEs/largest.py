##
#  This program reads a sequence of values and prints them, marking the 
#  largest value.
#  and the smallest number
#

# Create an empty list.
values = []

# Read the input values.
user_input = input("Please enter values, Q to quit: ")
while user_input.upper() != "Q" :
   values.append(float(user_input))
   user_input = input("Please enter values, Q to quit: ")

# Algo to find the largest value.
largest = values[0]
for i in range(1, len(values)) :
   if values[i] > largest :
      largest = values[i]

# Algo to find the smallest value.
smallest = values[-1]
for i in range(1, len(values)) :
   if values[i] < smallest :
      smallest = values[i]

# NOTE: This is faster, and ok to use if you just need to find the value...
largest = max(values)
smallest = min(values)
# note: There are other functions that work on lists, i.e. min, sum, and sort

# Print all values, marking the largest and smallest.
for element in values:
   print(element, end="")
   if element == largest :
      print(" <== largest value", end="")
   if element == smallest:
      print(" <=== smallest vaule", end="")
   print()


