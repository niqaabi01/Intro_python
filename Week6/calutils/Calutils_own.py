# Calutils.py without the use of the test mod
# Saaniah Blankenerg
# 2020/06/09

# option 1 test leap year
def is_leap_year():
    x = int(input("Enter year : "))
    if x % 4 == 0:
        if x % 100 == 0:
            if x % 400 == 0:
                print("The year ", x, "is a Leap year ")
            else:
                print(" The year", x, "is not a Leap year")
        else:
            print(" The year", x, "is a Leap year")
    else:
        print("The year ", x, "is not a Leap year ")


# option 2 test month name
def month_name():
    x = int(input("Enter month: "))
    while x <= 12:
        month = x - 1
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]
        num = months[month]
        print("Month number ", x, "is", num)
        x = x + 1


# option 3 test days in month
import calendar
def days_in_month():
    year = int(input("Enter year: "))
    x = year
    month = int(input("Enter month: ")) - 1
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    num = months[month]
    if num in ["January", "March", "May", "July", "August", "October", "December"]:
        print(num, "has 31 days")
    if num in ["April", "June", "September", "November"]:
        print(num, "has 30 days")
    if num in ["February"]:
        if calendar.isleap(x):
            print(num, "had 29 day")
        else:
            print(num, "has 28 days")


# option 4 find the first day of the given year
# import date.time library
import datetime
def first_day_of_year():
    year = int(input("Enter the year ? "))
    a = datetime.datetime(year, 1, 1)
    print("starting day of the year", year, "is", a.strftime("%A"))
    


# option 5 first day of month
def first_day_of_month():
    year = int(input("Enter the year ? "))
    month = int(input("Enter the month? "))
    a = datetime.datetime(year, month, 1)
    print("starting day is", a.strftime("%w"), "which is", a.strftime("%A"))


def Calutils_module():
    print("Choose from the following options :")
    print("0. Quit")
    print("1. Test_is_leap_year().")
    print("2. Test_month_name().")
    print("3. Test_days_in_month().")
    print("4. Test_first_day_of_year().")
    print("5. Test_first_day_of_month().")

    x = int(input("  "))
    while x != 0:
        if x == 1:
            is_leap_year()
            return Calutils_module()
        if x == 2:
            month_name()
            return Calutils_module()
        if x == 3:
            days_in_month()
            return Calutils_module()
        if x == 4:
            first_day_of_year()
            return Calutils_module()
        if x == 5:
            first_day_of_month()
            return Calutils_module()
        if x == 0 :
            break

Calutils_module()