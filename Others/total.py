##
#  This program reads a file containing numbers and writes the numbers to 
#  another file, lined up in a column and followed by their total and average.
#

# Prompt the user for the name of the input and output files.
inputFileName = input("Input file name: ")
outputFileName = input("Output file name: ")

# Open the input and output files.
infile = open(inputFileName, "r")
outfile = open(outputFileName, "w")

# Read the input and write the output.
total = 0.0
count = 0

line = infile.readline()
while line != "" :
   value = float(line)
   outfile.write(f"{value:15.2f}\n")
   total = total + value
   count = count + 1
   line = infile.readline()

# Output the total and average.
outfile.write(f"{'--------':>15s}\n")
outfile.write(f"Total: {total:8.2f}\n")

avg = total / count
outfile.write(f"Average: {avg:6.2f}\n")

# Close the files.
infile.close()
outfile.close()

