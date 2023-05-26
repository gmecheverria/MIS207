#
#  Calculates the area of a circle when given a radius
#

from math import pi  # imports pi from the math module

# Computes the area given the radius from the input
radius = int(input("To calculate the area of circle\nGive a radius:"))
area_of_circle = pi * radius ** 2
print(f"The area of the circle with radius = {radius:<2}is{area_of_circle: 5,.2f}")
