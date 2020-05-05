#By Daliah Aljutayli
#Python Program to Find LCM (Least Common Multiple)
#----------------------------


def LCM(num1,num2):
    if num1>num2:
        g=num1
    else: g=num2
    
    while True:
        if ((g%num1==0) and (g%num2==0)):
            LCM=g
            break
        g+=1
    return LCM
        

    


num1=int(input('Enter 1st Number: '))
num2=int(input('Enter 2nd Number: '))

print('LCM=', LCM(num1,num2) )
