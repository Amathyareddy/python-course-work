'''

#Working with Dates

#Getting the Current date & Extracting Year, Month, and Day & Finding the Day of the Week

from datetime import date,time,datetime,time

t = date.today()

print(t)
print("Year:", t.year)
print("Month:", t.month)
print("Day:", t.day)
print("Weekday from 0:", t.weekday())
print("Weekday from 1:", t.isoweekday())



#We get the ValueError: month must be in 1..12, not 13
#The months must be in 1-12 only

from datetime import date,time,datetime,time

t = date(2026,13,30)

print(t)



#Working with Time

#Creating a Specific Time


t = time(23,59,0)

print(t)



#Working with Date and Time Together

#Getting the Current Date and Time

from datetime import date,time,datetime,time

n = datetime.now()

print(n)
print("Year:", n.year)
print("Month:", n.month)
print("Day:", n.day)
print("Hour:", n.hour)
print("Minute:", n.minute)
print("Second:", n.second)



#Formatting Dates and Times

#Formatting Examples

from datetime import date,time,datetime,time

n = datetime.now()

print(n.strftime('%d/%m/%y'))
print(n.strftime('%d/%m/%y %H:%M:%S'))
print(n.strftime('%d/%m/%y %I:%M:%S %p'))
print(n.strftime('%d %b %y %I:%M:%S %p'))
print(n.strftime('%d %B %Y %I:%M:%S %p'))
print(n.strftime('%a, %d %B %Y %I:%M:%S %p'))
print(n.strftime('%A, %d %B %Y %I:%M:%S %p'))



#Code Description Example

Code     Description            Example
%Y        Full Year             2024
%m        Month (01-12)         02
%d        Day (01-31)           16
%H        Hour (00-23)          14
%I        Hour (01-12)          02
%M        Minutes (00-59)       30
%S        Seconds (00-59)       15
%p        AM/PM                 PM
%A        Full Weekday Name     Friday
%B        Full Month Name       February



#Date and Time Arithmetic

from datetime import date,time,datetime,timedelta

n = datetime.now()

n15 = n + timedelta(minutes=15)
n2 = n + timedelta(hours=2)
n7 = n + timedelta(days=60)

print(n15,n2,n7,sep='\n')

'''



