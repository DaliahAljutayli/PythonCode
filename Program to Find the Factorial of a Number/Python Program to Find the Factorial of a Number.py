#By Daliah Aljutayli
#Python Program to Find the Factorial of a Number
#Help: schoolarabia.net

Fnumber=1
number = int(input('Enter number= '))
print(number,'!',end='')

if number >=0:
    for i in range(1,number+1):
        Fnumber=Fnumber*i
        
print('=',Fnumber)
    
