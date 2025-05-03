#!/usr/bin/env python3

'''
OPS445 Assignment 1
Program: assignment1.py 
The python code in this file is original work written by
"Greemesh Basnet". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Author: Greemesh Basnet
Semester: Summer 2024
Description: This is Assingment 1 Final Milestone Version C.
'''

import sys

def day_of_week(date: str) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    day, month, year = (int(x) for x in date.split('/'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + day) % 7
    return days[num]

def leap_year(year: int) -> bool:
    "return true if the year is a leap year"
    ...
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    ...
   if month == 2:
        if leap_year(year):
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def after(date: str) -> str: 
    '''
    after() -> date for next day in DD/MM/YYYY string format

    Return the date for the next day of the given date in DD/MM/YYYY format.
    This function has been tested to work for year after 1582
    '''
    day, mon, year = (int(x) for x in date.split('/'))
    day += 1  # next day
    mon_max_day = mon_max(mon, year)
    
    if day > mon_max_day:
        day = 1
        mon += 1
        if mon > 12:
            mon = 1
            year += 1
    return f"{day:02}/{mon:02}/{year}"

def before(date: str) -> str:
    "Returns previous day's date as DD/MM/YYYY"
    ...
    day, mon, year = (int(x) for x in date.split('/'))
    day -= 1

    if day < 1:
        mon -= 1
        if mon < 1:
            mon = 12
            year -= 1
        day = mon_max(mon, year)
    return f"{day:02}/{mon:02}/{year}"

def usage():
    "Print a usage message to the user"
    print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY NN")
    sys.exit()

def valid_date(date: str) -> bool:
    "check validity of date"
    ...
     if len(date) != 10:
        return False
    
    if date[2] != '/' or date[5] != '/':
        return False
    
    day_str = date[0:2]
    mon_str = date[3:5]
    year_str = date[6:10]

    for char in day_str + mon_str + year_str:
        if char < '0' or char > '9':
            return False
        
    day = int(day_str)
    mon = int(mon_str)
    year = int(year_str)
    
    if mon < 1 or mon > 12:
        return False
    
    if day < 1 or day > mon_max(mon, year):
        return False
    
    return True
    
def day_iter(start_date: str, num: int) -> str:
    "iterates from start date by num to return end date in DD/MM/YYYY"
    ...
date = start_date
    while num != 0:
        if num > 0:
            date = after(date)
            num -= 1
        elif num < 0:
            date = before(date)
            num += 1
    return date


if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
    start_date = sys.argv[1]
    if not valid_date(start_date):
        usage()
    try:
        num = int(sys.argv[2])
    except:
        usage()
    end_date = day_iter(start_date, num)
    print(f'The end date is {day_of_week(end_date)}, {end_date}.')
  
