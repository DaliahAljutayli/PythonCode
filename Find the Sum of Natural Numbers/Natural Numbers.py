#By Daliah Aljutayli
#Python Program to Find the Sum of Natural Numbers
#--------------------------------------------
#Natural numbers are the positive integers or non-negative integers
#which starts from 1 and ends at infinity


number = int(input('Enter a Number: '))

if number >0:
    
    Sn=(number*(number+1))/2
    print('Sn= {0:.0f}'.format(Sn))
else:
    print('Not a Natural Number')
