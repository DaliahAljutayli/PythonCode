#By Daliah Aljutayli
#Python Program to Check Armstrong Number
#-------------------------------------
#A number is called Armstrong number (Narcissistic number) if it is equal to
#the sum of the cubes of its own digits.

s=0
t=number = int (input('Enter a Number: '))

## find the sum of the cube of each digit
while t>0:
    digit=t%10
    s=s+digit**3 #add digits after power by 3
    t//=10

# display the result
if number==s:print(number,'-> is an Armstrong number')
else: print(number,'-> is Not')

