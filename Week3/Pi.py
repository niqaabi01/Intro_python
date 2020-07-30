#soling pi using while loop and then applying it to find the Area of a circle 
#Saaniah Blankenberg
#21/05/2020

import math
print("Approximate value of pi ", math.pi.__round__(3))
r = float(input("Enter the radius of the circle : "))
area = math.pi * r * r

print("Area of the circle is : %.3f" %area)

#second method

from math import sqrt

root = 2*(2/sqrt(2))
denominator = sqrt(2)
pi = root
while 2 / sqrt(2 + denominator) > 1:
    pi = pi * 2 / sqrt(2 + denominator)
    denominator = sqrt(2 + denominator)
print("Approximation of pi: %s" % (round(pi, 3)))
R = float(input(" Enter the radius : "))
Area = pi * R * R
print("The Area in of the circle is : ", Area.__round__(3))

# Third method
import math

iterations = 28
numerator = 0.0
pi = 1.0
for i in range(1, iterations + 1):
    numerator = math.sqrt(2.0 + numerator)
    pi *= (numerator / 2.0)
pi = (1.0 / pi) * 2.0
print("Approximation of pi: %s" % (round(pi, 3)))
R = float(input(" Enter the radius : "))
Area = pi * R * R
print("The Area in of the circle is : ", Area.__round__(3))