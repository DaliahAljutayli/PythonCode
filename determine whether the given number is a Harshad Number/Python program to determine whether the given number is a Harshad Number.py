#By Daliah Aljutayli
#Python program to determine whether the given number is a Harshad Number
#---------------------------------
#If a number is divisible by the sum of its digits, then it will be known as a Harshad Number.

def harshad(num):
    sum=0
    temp=num
    while num>0:
        digit=num%10
        sum=sum+digit
        num=num//10
        
    if temp%sum==0:
        print(temp,' is a Harshad Number')
    else:print(temp,' is NOT a Harshad Number')
    
#-------------------- 
num= int(input('Enter a Number: '))

if num>=1:
    harshad(num)
else:print('Enter a Positive Number...')
