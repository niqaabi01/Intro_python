#calculating the area and perimeter of a triangle
#Saaniah Blankenberg
#18/05/2020



from math import sqrt

a = float(input(" Enter the length of the first side : "))
b = float(input(" Enter the length of the second side : "))
c = float(input(" Enter the length of the third side : "))

#calculate the semi-perimeter
S = (a + b+ c) /2
#calculate the area
Area = sqrt(S * (S - a) * (S - b) * (S - c))
print("The area of a triangle with side a the length of " + str(a) + " and side b the length of " + str(b)
    + " and side c with the length of " +str(c) + " is " + str(Area))
