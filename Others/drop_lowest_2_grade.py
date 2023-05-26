
grades = []
done = False
while not done:
    grade = float(input("Enter a mark (any negative number exit: "))
    if grade < 0:
        done = True
    else:
        grades.append(grade)

# drop the lowest
if len(grades) >= 2:
    grades.remove(min(grades))

# drop the next lowest
if len(grades) >= 2:
    grades.remove(min(grades))

# print the average
if len(grades) > 0:
    print(f'Your average with the lowest removed is {sum(grades)/len(grades):.2f}.')
else:
    print("Error: You must enter at least one grade.")
