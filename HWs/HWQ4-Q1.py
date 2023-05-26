#
# Write a program that asks the user for a number of rows and a number of columns.
# Print to the screen a rectangle with an alternating pattern of X's and O's.
#

# Gets users input
rows = int(input("Enter num of rows: "))
columns = int(input("Enter num of columns: "))

# Prints a rectangle of X's and O's
for r in range(rows):
    for c in range(columns):
       if r % 2 == c % 2:
           print("X", end="")
       else:
           print("O", end="")
    print()
