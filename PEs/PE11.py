#
# Ask users to enter a text
#

# Gets the users input
text = input("Enter a text:")

# Keeps the all the text lower
text = text.lower()

# Prints number of times the word "the" occurs in the text
print(text.count("the"))

if text.find("apple"):
    print(text.upper())
    print(text.lower())
