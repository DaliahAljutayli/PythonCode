#By Daliah Aljutayli
#Python Program to check if a Number is Positive, Negative or Zero

choice = input('Any letter to stanrt or x to Exit!\n')

while choice!='x':
   number =input('Enter a Number or x to Exit\n') #ask for str of finish 
   if number!='x':
      
      number=float(number) #convert str into float
      
      if number==0:
         print('A Zero'.format(number))         
      elif number>0:
         print('A Positive Number'.format(number))         
      else:
         print('A Negative Number'.format(number))
      
   else:
      print('Exit')#end if by x
      break
