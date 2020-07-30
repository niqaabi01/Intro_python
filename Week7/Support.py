#creating an automated tech response to single inputs = key words 
#Saaniah Blankenberg 
#2020/06/17


def intro():
    print('Welcome to the automated technical support system.')
    print('Please describe your problem.')


def add_input():
    return input().capitalize()


def main():
    intro()
    problem = add_input()
    responses = {
    "Crashed" : "Are the drivers up to date",
    "Blue" : "Ah, the blue screen of death. And then what happened?",
    "Hacked" : "You should consider installing and anti-virus software.",
    "Bluetooth" : "Have you tried mouthwash?",
    "Windows" : "Ah, I think I see your problem.What version?",
    "Apple" : "You mean the computer kind?",
    "Spam" : "You should see if your mail client can filter messages",
    "Connection" : "Telkom"}

    while problem != "Quit":
      if problem not in responses:
           print("Curious, Tell me more")
           problem = add_input()
      if problem in responses:
        print(responses.get(problem))
        problem = add_input()
      

print(main())
if __name__ == '__main__': main()
