#
# Create and test a new function called circle_area
# function must have one parameter that accepts the radius of a circle
# and produce a return value that is the area of a circle with the given radius.
#

# import math to be able to use pi
import math

# Creates the function to calculate the area
def circle_area(radius):
    area = math.pi * radius ** 2
    return area

# gets users input and prints the area of the circle
ans = float(input("Enter a radius: "))
area = circle_area(ans)
print(f"The area of the circle is {area:.2f} with a radius of {ans}")
