#By Daliah Aljutayli
#Python Program to Print the Fibonacci sequence
import math

s1=0; s2=1;i=2
n =int(input('n= '))
# 1st:
x=((math.pow(1+(math.sqrt(5)),n))-(math.pow(1-(math.sqrt(5)),n)))/(math.pow(2,n)*math.sqrt(5))
print('F({0:.0f})={1:.1f}'.format(n,x))

# 2nd
if n<=0:print('\nEnter a Positive Number')
elif n==1:print("\nFibonacci sequence:",n)
else:
    print('\nFibonacci sequence:',s1,s2,end=" ")
    while i<=n:
        N=s1+s2
        print(N,end=' ')
        s1=s2
        s2=N
        i+=1
