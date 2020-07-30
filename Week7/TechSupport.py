# creating an automated responce that checks for key words in the user input
# Saaniah Blankenberg
# 2020/06/18
def intro():
    print('Welcome to the automated technical support system.')
    print('Please describe your problem.')


def add_input():
    return input().lower()


def main():
    intro()
    question1 = add_input()

    responses = {
        "crashed": "Are the drivers up to date",
        "blue": "Ah, the blue screen of death. And then what happened?",
        "hacked": "You should consider installing and anti-virus software.",
        "bluetooth": "Have you tried mouthwash?",
        "windows": "Ah, I think I see your problem.What version?",
        "apple": "You mean the computer kind?",
        "spam": "You should see if your mail client can filter messages",
        "connection": "Telkom"}
    issues_list = {"crashed", "blue", "hacked", "bluetooth", "windows", "apple", "spam", "connection"}
    # to check for a word in a string matching word in list

    while (not question1 == "quit"):
        input_words = question1.split()
        for i in range(0, (len(input_words))):
            if input_words[i] in issues_list:
                print(responses[input_words[i]])
                break
            elif i == (len(input_words) - 1):
                print("Curious, Tell me more")

        question1 = add_input()


main()
if __name__ == '__main__': main()