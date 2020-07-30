name = input("enter your name : ")
secret_num = 17
guess = ""
print("HINT- the number ranges from 0 to 20")

while guess != secret_num:
    guess =eval(input("enter your guess? "))
    if guess < secret_num:
        print("too low")
    elif guess > secret_num:
        print("too high")
else:
    print("Well done!!!!" + name+ " You are correct")