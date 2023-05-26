#
# prompts a user for a phrase
# displaying it with a box of #'s characters around it.
#

# Title
print("Displays a box of #'s characters around the phrase")

# Gets the users input
phrase = input("Enter a phrase:")

# Computes the box of #'s characters around the phrase
phrase = "# " + phrase + " #"
box = len(phrase) * "#"

# Prints the results
print('\n' + box + '\n' + phrase + '\n' + box)
