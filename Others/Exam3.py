infile = open('contacts.csv', "r")
outfile = open('contacts.csv', "w")

line = infile.readline()
done = False
print("To stop enter !")
while not done:
    name = input("Enter the name: ")
    phone_num = input("Enter phone number ###-###-####: ")
    outfile.write(f"{name:s}, {phone_num:s}\n")
    if name == "!":
        done = True
    line = infile.readline()

infile.close()
outfile.close()