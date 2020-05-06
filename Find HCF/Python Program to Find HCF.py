#By Daliah Aljutayli
#Python Program to Find HCD of GCD
#----------------------
# Greatest Common Divisor (GCD) -> HCD

def HCF(num1,num2):
    if num1>num2:
        s=num2
    else: s=num1
    
    for i in range (1,s+1):
        if (num1%i==0) and (num2%i==0):
            HCF=i
    return HCF
        
num1=int(input('Enter 1st Number: '))
num2=int(input('Enter 2nd Number: '))

print('HCF=', HCF(num1,num2) )
