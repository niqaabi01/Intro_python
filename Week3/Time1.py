# find the first day of the given year
#Saaniah Blankenberg
#18/05/2020

print("NOTE : only use whole numbers, no decimal values")
hours = int(input(" Enter the hours : "))
minutes = int(input(" Enter the minutes : "))
seconds = int(input(" Enter the seconds  : "))


def check_range(time):
    if hours in range(0, 24):
        pass
        if minutes in range(0, 60):
            pass
            if seconds in range(0, 60):
                print("your time is valid")
            elif seconds not in range(0, 60):
                print("your time is invalid")
        elif minutes not in range(0, 60):
            print("your time is invalid")
    elif hours not in range(0, 24):
        print("your time is invalid")
print(check_range(hours))