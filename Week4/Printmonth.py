#Printing months using 6 row by 7 column outputs
#Saaniah Blankenberg
#27 May 2020

day = input("Enter day of the week: ")
month = input("Enter month: ")

if month in ["January", "March", "May", "July", "August", "October", "December"]:
    x = 31
elif month in ["February"]:
    x = 28
else:
    x = 30

DAY_OFF = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
off = DAY_OFF.index(day)

print(month)
print("Mo Tu We Th Fr Sa Su")
for i in range(off):
    print("  ", end=' ')
for i in range(x):
    print("%2d" % (i + 1), end=' ')
    if (i + off) % 7 == 6: print()