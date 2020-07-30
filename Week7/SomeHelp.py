#creating an automated tech response
#Saaniah Blankenberg 
#2020/06/17
#somehelp.py 

def intro():
    print('Welcome to the automated technical support system.')
    print('Please describe your problem.')


def add_input():
    return input().lower()


def main():
    import random
    intro()
    question = add_input()
    outcomes = ["Have you tried it on a different operating system? ", "Did you reboot it? ", "What colour is it? ",
                "You should consider installing anti-virus software.", "Contact Telkom. ",
                "I should get that looked at if I were you. "]
    while question != "quit":
        num = random.randint(0, 5)
        print(outcomes[num])
        question = add_input()


main()

if __name__ == '__main__': main()