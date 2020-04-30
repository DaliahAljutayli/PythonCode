#By Daliah Aljutayli
#Python program to swap two variables


var1 = input('1st Variable: ')
var2 = input('2nd Variable: ')

swap=var1
var1=var2
var2=swap

print('''\nVariables After Swap:
First Variable : {}
Second Variable: {}
'''.format(var1,var2) )
