#By Daliah Aljutayli
#Python Program to Find Factorial of Number Using Recursion
#--------------------------------------------------


def fact(i):
    if i==1:
        return i
    else:
        return i*fact(i-1)

#-------------------------------
i = 1
number = int(input('Enter number= '))
print(number,'!',end='')

if number <=0:
    print('Sorry, Enter a Positive Number')

else:
    for i in range(1,number+1):
        fact(i)
    print(fact(i))
        

