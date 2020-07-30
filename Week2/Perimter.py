w1 = float(input("Enter width 1 ?"))
h1 = float(input("Enter height 1 ?"))
w2 = float(input("Enter width 2 ?"))
h2 =float(input("Enter height 2 ?"))
price_per_meter =float (input("price of fencing per meter ?"))

width = 2 * (w1 + w2)
height = 2 * (h1) 

perimeter = width + height

result: float = perimeter * price_per_meter
print(" the total fence required in meters=  "+str(perimeter))
print("the total cost of the fence is R" +str(result))