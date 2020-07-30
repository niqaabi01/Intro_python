#inputing a number and getting 7 numbers in sequence in a row with a space between each
#Saaniah Blankenberg
#26 May 2021


n = int(input("Enter the start number: "))
v = -6 < n < 93
while v <= n:
    outcome = v + n -1
    print(outcome, sep='  ', end='  ', flush=True)

    v = v + 1
    if v == 8:
        break