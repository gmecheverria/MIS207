#
# Write a program that asks a user for a number of rows and a number of columns
# Then prints to the screen a rectangle of # characters.
#

# Gets users input
rows = int(input("Enter num of rows: "))
columns = int(input("Enter num of columns: "))

# Prints a rectangle of # characters
for r in range(rows):
    for c in range(columns):
        print("#", end="")
    print()
