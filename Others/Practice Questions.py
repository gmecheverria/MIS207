#
#  Exam 1 Practice Question
#  Question 1
#

# Title
print("\nWelcome to the BigBox Store Sale Event!\n")

# get user input
total = float(input("What is your total of your purchase? "))
member = input("Are you a part of the BigBox Preferred Customer Y or N?")

# print results
if member.upper() == "Y":
    if total >= 500:
        discount = 0.30
    elif total >= 100:
        discount = 0.15
    else:
        discount = 0
else:
    if total >= 500:
        discount = 0.20
    elif total >= 100:
        discount = 0.10
    else:
        discount = 0
print(f"\nThe total discount you will receive for this order is ${total*discount:,.2f} resulting in a new total" + f" of ${total*(1-discount):,.2f}.")

# say goodbye
print("\nThank you for shopping at Bigbox. Have a nice day!")


#
#  Question 2
#

# title
print("\nWelcome to the financial calculator program\n")

# process user input
choice = input("Please enter your choice of calculation: FV (future value of an investment), or PV (present value):")
rateReturn = float(input("What is your rate of return per term? "))
numberTerms = float(input("What is the number of terms the investment is held? "))

# calculate result
if choice.upper() == "FV":
    presentValue = float(input("What is your present value of your investment? "))
    futureValue = presentValue * (1 + rateReturn) ** numberTerms
    print(f"Your expects future value of current investment will be ${futureValue:,.2f}")
elif choice.upper() == "PV":
    futureValue = float(input("What do you want your future value of your investment to be? "))
    presentValue = futureValue / (1 + rateReturn) ** numberTerms
    print(f"To achieve your future value your present value of investments will need to be ${presentValue:,.2f}")
else:
    print("Invalid Input")

# print goodbye
print("\nHave a prosperous day!\n")



