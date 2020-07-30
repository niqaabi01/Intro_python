 # Calutils.py creating a module that tests various opperations based on input given by user.
 # Saaniah Blankenerg
 # 2020/06/12

# option 1 test leap year
def is_leap_year(year):
    if year%4 == 0:
        if year%100 ==0 and year%400 != 0:
            return False
        return True
    else:   
        return False

# option 2 test month name
def month_name(number):
    if number == 1:
        return 'January'
    elif number == 2:
        return 'February'
    elif number == 3:
        return 'March'
    elif number == 4:
        return 'April'
    elif number == 5:
        return 'May'
    elif number == 6:
        return 'June'   
    elif number == 7:
        return 'July'
    elif number == 8:
        return 'August'
    elif number == 9:
        return 'September'
    elif number == 10:
        return 'October'
    elif number == 11:
        return 'November'
    elif number == 12:
        return 'December'


# option 3 test days in month
def days_in_month(month_number,year):
    if month_number in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month_number in {4, 6, 9, 11}:
        return 30
    elif month_number == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
      

# option 4 find the first day of the given year
def first_day_of_year(year):
        day_num = ((1 + 5*((year - 1)%4)) + 4*((year - 1)%100) + 6*((year - 1)%400))%7
        date = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        outcome = date[day_num]
        return outcome

# option 5 first day of month
def first_day_of_month(month_number, year):
    weekday_num =  ((1 + 5*((year - 1)%4)) + 4*((year - 1)%100) + 6*((year - 1)%400))%7
    day_num = 0
    for m in range(1, month_number):
        day_num += days_in_month(m,year)
        
    for i in range(1,day_num+1):            

        if weekday_num == 6:
            weekday_num = 0
        
        else:
            weekday_num += 1
            
    return weekday_num      
