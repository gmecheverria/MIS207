#
# Predicts if the Swans, Lancelot and Elaine, will mate
#
print("Predicts if the Swans will mate")

# Ask for the users input
temperature = float(input("What is the average temperature in March?"))

# Decides what the prediction will be
if temperature < 60:
    won = input("Did the Cyclones will against Iowa in the last season? Y or N")
    if won == "y":
        prediction = "mate"
    else:
        prediction = "not mate"
else:
    prediction = "mate"

# Prints the results
print("The Swans are predicted to", prediction)
