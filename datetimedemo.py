import datetime

today = datetime.datetime.today()
now = datetime.datetime.now()
print(today)
print(now)

# print date 

d = datetime.date(2026,10,29)
print(d)

# print time

t = datetime.time(16,50)
print(t)

# mock interview date 

today = datetime.date.today()
mock_date = datetime.timedelta(days=7)

mock_int_date = today + mock_date

print(mock_int_date)

# time module sleep function

import time

time.sleep(5)

print("Python Lab")

# calender module

import calendar

print(calendar.month(2026,10))

print(calendar.calendar(2026))