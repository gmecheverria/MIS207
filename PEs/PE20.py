#
# Write a program that asks a user for a number of grades (any negative value to stop).
# Store each grade in a list called grades.
# When the user indicates they are finished, display all of the grades, the sum or the grades, the min, the max,
# and the average grade.
#

grades = []  # list of the grades

done = False

# adds the grades into the list until user enters -1 to stop
while not done:
    num = float(input("Enter a grade or -1 to finish: "))
    grades.append(num)
    if num < 0:
        grades.remove(-1)
        done = True

# prints the grades user enters
print("List of grades", grades)

# prints sum of grades
print("Total sum of all the grades is", sum(grades))

# prints the min of grades
print("The min of all the grades is", min(grades))

# prints the max of the grades
print("The max of all the grades is", max(grades))

# prints the average of the grades
print("The average of all the grades is", sum(grades) / len(grades))







