#By Daliah Aljutayli
#Python Program to Check Armstrong Number

import math

s=r=0
tem=number = int (input('Enter a Number: '))

while tem>0: # 153 >0
    s=s+(math.pow((tem%10),3)
    tem//=10
    
# display the result
if number==s:
    print(number,'-> is an Armstrong number')
    
else:
    print(number,'-> is Not an Armstrong number')

