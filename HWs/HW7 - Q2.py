#
# Write a program that asks the user for an input file name
# and then displays to the screen the number of non-blank lines found in the file.
#

done = False

while not done:
    # Used so the program does not crash if an error occurs
    try:
        # Prompt the user for the name of the input and output files.
        inputFileName = input("Input file name: ")
        outputFileName = input("Output file name: ")

        # Open the input and output files.
        infile = open(inputFileName, "r")
        outfile = open(outputFileName, "w")

        # Read the input and write the output.
        count = 0
        for line in infile:
            count += len(line.split())
        print(count)

        # Output the count of non-blank lines found in the file
        outfile.write(f"{count}\n")

        # Close the files.
        infile.close()
        outfile.close()

    except FileNotFoundError:
        print("The file was not found. Try again. Enter a filename.")

    # Used to stop the while loop
    else:
        break

