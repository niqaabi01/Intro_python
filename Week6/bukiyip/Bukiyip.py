# bukiyip.py base 3 counting mthod
# Saaniah Blankenberg
#2020/06/12
#converting base 3 into a decimal num #OPTION b
def bukiyip_to_decimal(a):
    num =str(a)
    index = 0
    decimal = 0
    for i in range(len(num)-1,-1,-1):
        decimal += int(num[i])*3**(index)
        index += 1
    return decimal


# converting decimal num into base 3 #OPTION d
def decimal_to_bukiyip(a):
    quotient = a/3
    remainder = a%3
    if quotient == 0:
        return " "
    else:
        return decimal_to_bukiyip(int(quotient))+str(int(remainder))



#adding 2 bukiyup numbers#OPTION a
def bukiyip_add(a,b):
  
    a_10 = bukiyip_to_decimal(a)
    b_10 = bukiyip_to_decimal(b)
    product_10 = a_10 + b_10
    product = decimal_to_bukiyip(product_10)
    return product



#multiplying 2 bukiyup numbers#OPTION m
def bukiyip_multiply(a,b):
    a_10 = bukiyip_to_decimal(a)
    b_10 = bukiyip_to_decimal(b)
    product_10 = a_10 * b_10
    product = decimal_to_bukiyip(product_10)
    return product