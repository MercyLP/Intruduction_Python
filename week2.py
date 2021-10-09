#Lecture code for Week2
#https://www.programiz.com/python-programming

my_string = 'baldan'
type(my_string)

my_int = -15
type(my_int)

my_float = 15.78
type(my_float)

my_boolen = True
type(my_boolen)

import datetime
today = datetime.date.today()
today

today.year
today.month
today.day

datetime.datetime.strptime('2021-01-22', '%Y-%m-%d') # Convert string to datetime

today.strftime('%Y-%m-%d') # Convert datetime to string


