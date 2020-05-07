#By Daliah Aljutayli
#Python Program to Convert Decimal to Binary, Octal and Hexadecimal
#Help: geeksforgeeks.org
#----------------------

def desTbin(Decimal):
    if Decimal>1:
        desTbin(Decimal//2)
    print(Decimal%2,end='')
    

def desToct(Decimal):
    if Decimal>1:
        desToct(Decimal//8)
    print(Decimal%8,end='')
    

def desThex(Decimal):
    if Decimal>1:
        desThex(Decimal//16)
    print(Decimal%16,end='')
#-------------------------------
Decimal  = int (input('Enter a Decimal Number: '))

print('Using a Function:')
desTbin(Decimal)
print('\n')
desToct(Decimal)
print('\n')
desThex(Decimal)

print('\n-------------------\nUsing a built-in functions')
print('Binary= ',bin(Decimal))
print('Octal= ',oct(Decimal))
print('Hexadecimal= ',hex(Decimal))
