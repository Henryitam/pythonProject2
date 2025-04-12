from datetime import datetime
import calendar


def days_spent(da1, da2):
    date_format = "%Y-%m-%d"
    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)
    differ = abs((d2 - d1).days)
    return differ

def days_of_the_year(year):
    total_day = 0
    for month in range(1,13):
        total_day += calendar.monthrange(year,month)[1]
    return total_day


date1 = input("enter the date of the firstday of the year")
date2 = input("enter todays date (yyyy-mm-dd):")
year1 = 2025

difference = days_spent(date1, date2)

final = days_of_the_year(year1)
remains = final - difference
print(f"the nunber of days remaining is {remains}, make good use of it")