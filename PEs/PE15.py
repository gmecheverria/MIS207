#
# Determines if the number is an iowan number
#

# gets the users input
phoneNum = input("Enter your phone number in the form of (555)555-5555: ")

# get the index for the area code
areaCode = phoneNum[1]+phoneNum[2]+phoneNum[3]

# prints whether the phone number is an iowan number or not
if areaCode == "319" or areaCode == "515" or areaCode == "563" or areaCode == "641" or areaCode == "712":
    print("The phone number is an Iowan number")
else:
    print("The phone number is not an Iowan number")