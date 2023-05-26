##
#   This program reads a sequence of die toss values and prints how many times
#   each value occurred.
#   Alter this file so that it’s a simulation – the user doesn’t enter any
#   values, instead the program will generate 1000 rolls of a die and store
#   this in a list.
#   Once this list is generated, display the results of the value counts (use
#   the printCounters method in the dice.py program)
#
import random

def main() :
   counters = countInputs(6)
   printCounters(counters)
   
## Reads a sequence of die toss values between 1 and sides (inclusive) 
#  and counts how frequently each of them occurs.
#  @param sides the die's number of sides 
#  @return a list whose ith element contains the number of times the value i
#  occurred in the input. The 0 element is unused.
#
def countInputs(sides) :
   counters = [0] * (sides + 1)   # counters[0] is not used.

   for i in range(1000):
      value = random.randint(1,6)
      counters[value] = counters[value] + 1
   return counters

## Prints a table of die value counters.
#  @param counters a list of counters. counters[0] is not printed.
#
def printCounters(counters) :
   print(f"{'roll':^5}{'count':^5}")
   for i in range(1, len(counters)) :
      print(f"{i:^5d}{counters[i]:^5d}")

# Start the program.
main()

