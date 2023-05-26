#
# Write a program that reads the attached file called input.txt
# creates an output.txt file that a value to each row that is the total of all the values in the row.
# Each row of the file will consist of three integer values separated by a comma.
# You must create an output file that will have four values for each row,
# the first three values from the original file plus a new value that is the sum of the other three.
#

# Open the input and output files.
in_file = open('input.txt', 'r', encoding='utf-8')
out_file = open('output.txt', 'w', encoding='utf-8')

# Read the input and write the output.
txt = in_file.read()
lines = txt.splitlines()
for line in lines:
    if ',' in line:
        num1, num2, num3 = line.split(',')
        total = int(num1) + int(num2) + int(num3)
    out_file.write(line + "," + str(total) + '\n')

# Close the files.
in_file.close()
out_file.close()

