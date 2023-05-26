#
# Based on prior data, you've identified a range of revenue that a store generates per day.
# This range is from 31,956 to 48,345 dollars, and all values in this range have the same probability.
# Run a simulation that predicts the total revenue for the next 100 days in which the store is open.
#

# import random module to be able to use randint
import random

# explains what the simulation is
print("\nRun a simulation that predicts the total revenue for the next 100 days in which the store is open.")

# constant initial numbers
days = 100
total_revenue = 0

# creates the simulation that predicts the total revenue for specific number of days
for i in range(days + 1):
    revenue = random.randint(31956, 48345)
    total_revenue = total_revenue + revenue

# prints the predicted total revenue
print(f'\nThe total revenue is ${total_revenue:,.2f}')
