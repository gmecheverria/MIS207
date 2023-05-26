##
#  A program to compute shipping costs.
#

# Obtain the user input.
country = input("Enter the country: ")
state = input("Enter the state or province: ")

# Compute the shipping cost.
shipping_cost = 0.0

if country == "USA":
   if state == "AK" or state == "HI":  # See Section 3.7 for the or operator
      shipping_cost = 10.0
   else:
      shipping_cost = 5.0
else:
   shipping_cost = 10.0

# Print the results.
print(f"Shipping cost to {state}, {country}: ${shipping_cost:.2f}")

