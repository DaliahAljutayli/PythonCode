#By Daliah Aljutayli
#Python Function to Display Calendar
#----------------------------

import calendar
import datetime 

calendar.setfirstweekday(calendar.SUNDAY) #1st day is Sunday

def DayName(): #display Weekday name
    d = datetime.datetime.now()
    print(d.strftime('%A , %a')) # %A -> Weekday,full version %a -> short version

def A_DayTime(): #display current day and  time
    print(datetime.datetime.now())

def Mnth():# display the entered month and calender of the year
   month= int(input('Month is: '))
   year = int(input('Year is: '))
   print(calendar.month(year,month))

def All_Years(): #display all months of entered year
   year = int(input('Year is: '))
   print(calendar.calendar(year))    


choice = int(input('''Display:
1- The name of weekday
2- The day and Time
3- Name of Month with Year
4- All Monthes of a Year\n'''))

if choice==1:DayName()
elif choice==2:A_DayTime() 
elif choice==3:Mnth()
elif choice==4:All_Years()

else: print('Not a Choice!')
