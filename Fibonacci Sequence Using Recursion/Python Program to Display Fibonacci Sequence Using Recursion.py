#By Daliah Aljutayli
#Python Program to Display Fibonacci Sequence Using Recursion
#------------------------------------------

def fibonacci(n):
    if n<=1: # first terms are 0 and 1 
        return n
    else: #obtain sequence by adding their preceding two numbers
        return(fibonacci(n-1)+fibonacci(n-2)) #

    

n =int(input('Enter n= '))


if n<=0:print('\nEnter a Positive Number')
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(fibonacci(i)) #Recursion a function

