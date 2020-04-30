#By Daliah Aljutayli
#Python program to convert Celsius to Fahrenheit
#Help: rapidtables.com

choice = float(input('''choice:
1- Celsius to Fahrenheit
2- Fahrenheit to Celsius
'''))


if choice==1:
   degree=float(input('Celsius='))
   degree=degree*(9/5)+32
   print('{0:.2f} Fْ '.format(degree))
   
elif choice==2:
   degree=float(input('Fahrenheit='))
   degree=(degree-32)/(9/5)
   print('{0:.2f} Cْ '.format(degree))

else: print('Not a choice!')
