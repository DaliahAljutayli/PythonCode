#By Daliah Aljutayli
#Python program to print all pronic numbers between 1 and 100
#---------------------------------------
#A pronic number is a number which is the product of two consecutive integers
#that is, a number of the form n(n + 1). ... called oblong numbers
#_________________________________________________________

def pronic(i):
    temp=False
    for j in range(1,i+1):
        if i==(j*(j+1)):
            temp=True
            break
    return temp


#num = int (input('Enter Number: '))

print('Displays pronic numbers between 1 and 100:\n')
for i in range(1,101):
    if pronic(i):
        print(i,end=' ')
