#By Daliah Aljutayli
#Python Program to Print all Prime Numbers between an Interval
#Help: geeksforgeeks.org
#----------------------------

start = int (input('Start the range from: '))
end = int (input('End the range at: '))

for a in range (start,end+1):
    if a>1:
        for i in range (2,a):
            if (a%i)==0:
                break
        else:print(a,end=' ')
