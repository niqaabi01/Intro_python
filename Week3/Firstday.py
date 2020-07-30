# find the first day of the given year
#Saaniah Blankenberg
#21/05/2020

year = int(input("Enter the year: "))
year2 =int(input("Enter the second year: "))
date = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

while year <= year2:
    day = 1 + 5 * ((year - 1) % 4)
    day = day + 4 * ((year - 1) % 100)
    day = day + 6 * ((year - 1) % 400)
    day = day % 7
    outcome = date[day]
    print("The 1st of January of the year  ", year, "is ", outcome)
    year = year + 1