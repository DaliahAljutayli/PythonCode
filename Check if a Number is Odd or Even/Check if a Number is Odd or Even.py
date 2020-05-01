#By Daliah Aljutayli
#Python Program to Check if a Number is Odd or Even
#Help: mathsisfun.com


choice = input('Any letter to stanrt or x to Exit!\n')

while choice!='x':
   number =input('Enter a Number or x to Exit\n')  
   if number!='x':
      
      number=float(number) #convert str into float
      
      if (number%2)==0:
         print('An Event Number'.format(number))         
      elif (number%2)==1:
         print('An Odd Number'.format(number))         
      else:
         print('Error!!')
      
   else:
      print('Exit')#end if by x
      break
