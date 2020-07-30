name = input("enter your name : ")
secret_num = 17
guess = ""
print('HINT- the number ranges from 0 to 20')
motivator = " You'll get it next time "

while guess != secret_num:
    guess =eval(input("Can you guess the number? "))
    if guess < secret_num:
        print("Oh no, this is too low." + motivator +" Please try again")
    elif guess > secret_num:
        print("Oh no, this is too high" + motivator +"  Please try again")
else:
    print("Well done!!!!" + name+ " You did it" + "!!!!" + "You've guessed the Correct number ")