#outputing the palindrome prime numbers in a range
#Saaniah Blankenberg
#27 May 2020


start =int(input("Enter the start point: "))
end = int(input("Enter the end point: "))
start += 1
for i in range(start, end):
        y = True
        if(str(i) == str(i)[::-1]):
            if(i>2):
                for start in range(2,i):
                    if(i%start==0):
                        y = False
                        break
                if y:
                    print(i)
