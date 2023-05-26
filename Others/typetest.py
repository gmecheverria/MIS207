import math
# Testing different types in the same variable
taxRate = 5  # int
print(taxRate)
taxRate = 5.5  # float
print(taxRate)
taxRate = "Non-taxable"  # string
print(taxRate)
print(taxRate + str(5))


somelist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",  "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
for i in range(len(somelist)) :
   print(somelist[i], end = "")