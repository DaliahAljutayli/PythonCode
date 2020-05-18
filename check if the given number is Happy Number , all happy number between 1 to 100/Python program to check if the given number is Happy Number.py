#by Daliah Aljutaili
#Python program to check if the given number is Happy Number
#--------------------------------
##happy number is a number, where starting with any positive integers
##replace the number by the sum of squares of its digits, this process will
##be repeated until it becomes 1
#_________________________________________________________________

def HappyNumber(temp):
    sum=0
    while temp>=1:#Calculates the sum of squares of digits    
        digit=temp%10
        sum=sum+digit**2 #add digits after power by 2
        temp//=10
    return sum

temp=num = int(input('Enter Number: '))
sum=0

if num >1:
    while(temp!=1 and temp!=4):
        temp=HappyNumber(temp)
    if temp==1:print(num,' is A Happy Number')
    elif temp==4:print(num,' NOT A Happy Number - SAD Number')
        
elif num==1:print(num,' is a Happy Number') #Input 1 -> HuppeyNumber
else:
    print('Enter a positive number!')#Input Must 1 an up

print('\n All Happy Numbers Between 1 and 100 are:')
for i in range(1,101):
    re=i
    while(re!=1 and re!=4):
        re=HappyNumber(re)
    if re==1:print(i,end=' ')
    
