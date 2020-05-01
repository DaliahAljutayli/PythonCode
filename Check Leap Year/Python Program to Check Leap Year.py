#By Daliah Aljutayli
#Python Program to Check Leap Year
#--------------------------------------
#A normal year has 365 days.
#A Leap Year has 366 days (the extra day is the 29th of February)
#--------------------------------------
##Leap Years are any year that can be exactly divided by 4
##not except if it can be exactly divided by 100, then it isn't
##yes 	except if it can be exactly divided by 400, then it is



year = int (input('Enter The Year: '))

if (year%4)==0: #it can be exactly divided by 4   
   if (year%100)==0: 
       
      if (year%400)==0:print(year,' is a leap year')#it can be exactly divided by 400
      else:print(year,' is NOT a leap year')
      
   else:print(year,' is a leap year')#can't be  divided by 100   
else:print(year,' is NOT a leap year')
