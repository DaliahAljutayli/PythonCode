#By Daliah Aljutayli
#Python Program to Check Prime Number
#Help: geeksforgeeks.org
#----------------------------
#A Prime Number can be divided exactly only by 1 or itself

number = int (input('Enter The Number: '))

if number>1:
    for i in range (2,number//2):
        if (number%i)==0:
            print(number,' is Not prime number')
            break
    else:print(number,' is a Prime number')
else:print(number,' is Not prime number')
