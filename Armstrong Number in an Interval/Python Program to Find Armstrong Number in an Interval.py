#By Daliah Aljutayli
#Python Program to Find Armstrong Number in an Interval
#---------------------------------------------------
#A number is called Armstrong number (Narcissistic number) if it is equal to
#the sum of the cubes of its own digits.

start= int (input('Start from: '))
end= int (input('End at: '))

print('Armstrong numbers are= ',end=' ')
for num in range(start,end+1):
    s=0
    t=num
    while t>0:
        digit=t%10
        s=s+digit**3 #add digits after power by 3
        t//=10
        if num==s:
            print(num,end=' ')
