#
# Create a program that asks for student name, and input filename.
# The input file contains a list of grades (one per line).
# The program should read the grades, and output a file (named output.txt)
# that contains the student name, the list of grades (one per line), and the average grade.
#

# Prompt the user for the name of the input and output files.
inputFileName = input("Input file name: ")
outputFileName = input("Output file name: ")

# Open the input and output files.
infile = open(inputFileName, "r")
outfile = open(outputFileName, "w")

# Ask the user for the name and displays it
name = input("What is the student name? ")
outfile.write(f"{name:s}\n")

# Read the input and write the output.
total = 0.0
count = 0
line = infile.readline()
while line != "" :
   value = float(line)
   outfile.write(f"{value:.2f}\n")
   total = total + value
   count = count + 1
   line = infile.readline()

# Output the average.
outfile.write(f"{'--------':s}\n")
avg = total / count
outfile.write(f"Average: {avg:.2f}\n")

# Close the files.
infile.close()
outfile.close()
