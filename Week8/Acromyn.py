#using user input to creat an acronym 
# Saaniah Blakenberg
# 2020/06/22

ignore = input(" Enter words to be ignored separated by commas: ").split(', ')
sen = input("Enter a title to generate it's acronym: ").lower()
word_list = list(sen.split())
remove = " ".join([i for i in word_list if i not in ignore])
words = remove.split()
letters = [word[0] for word in words]
print("The acronym is: ", "".join(letters).upper())