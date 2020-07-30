width1 = float(input("enter width one : "))
height1 =float(input("enter height one : "))
width2 = float(input("enter width two : "))
height2 = float(input("enter height two :"))
cost_mp =float(input(" enter price per meter :"))

height = 2 * float(height1) 
width =  float(width1) + (width2)

def multiply(width):
    result = 2
    for index in range(1):
        result = result * width
    return result

total = height + multiply(width)

result = total * cost_mp
print("The total amount fencing per meter : " + str(total))
print(" The total cost of fencing R" + str(result))