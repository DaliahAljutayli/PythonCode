#By Daliah Aljutayli
#Python program to display calendar
#Help: geeksforgeeks.org and 

import calendar
calendar.setfirstweekday(calendar.SUNDAY) #1st day is Sunday


choice = int(input('''Display:
1- Just a Month
2- A Whole Year\n'''))

if choice==1:
   month= int(input('Month is: '))
   year = int(input('Year is: '))
   print(calendar.month(year,month))
   
elif choice==2:
   year = int(input('Year is: '))
   print(calendar.calendar(year))

else: print('Not a Choice!')
   
