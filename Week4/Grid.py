#creating grids using inputs and for loops in for loops
#Saaniah Blankenberg
#26 May 2020


n = int(input("Enter the start number: "))

if -6 < n < 2:
    for x in range(n, 37 - (n < -4), 7):
        for y in range(x,  x + 7):
            print("{:>2}".format(y), end=" ")
        print()