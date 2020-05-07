#By Daliah Aljutayli
#Python Program To Find ASCII value of a character


choice = input('1- for One Character \n2- More than One Characters\n')

if choice==1:
    value = input('Enter a Value:')
    print('The ASCII character of ',value,'is',ord(value)) #ord take 1 char


else:
    value = input('Enter a Value:')
    for i in range(len(value)):
        print('The ASCII character of %c is %d'%(value[i],ord(value[i])) )


