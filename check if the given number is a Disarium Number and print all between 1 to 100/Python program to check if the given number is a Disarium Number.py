#By Daliah Aljutayli
#Python program to check if the given number is a Disarium Number
#Python program to print all disarium numbers between 1 and 100 
#-------------------------------------------------------
#A Disarium number is a Sum of its digits powered with their
#respective position is equal to the original number
#__________________________________________________________________
def All_Disarium(a):
    temp=sum=0
    n=a
    leng=0
    while n!=0:
        leng+=1
        n=n//10    
    while a>0:
        temp=a%10
        sum+=(temp**leng)
        a=a//10
        leng-=1
    return sum
print('All Disarium Numbers between 1 and 100:')
for All in range(1,100):
    result=All_Disarium(All)
    if result==All:
        print(All,end=' ')
#_______________________________
s=0
t=number = int (input('\nEnter a Number: '))

## find the sum of each digit
while t>0:
    length=len(str(t))  #Length of number like: 173 length = 3
    digit=t%10
    s=s+int(digit**length) #add digits after power by length 1,2,3,...etc
    t//=10

# display the result
if number==s:
    print(number,' ->is a Disarium Number')    
else:
    print(number,'-> is not a Disarium Number')
