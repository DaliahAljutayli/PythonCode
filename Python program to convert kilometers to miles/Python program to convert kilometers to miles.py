#By Daliah Aljutayli
#Python program to convert kilometers to miles

value = float(input('''choice:
1- Kilometers to Miles
2- Miles to Kilometers
'''))

n = 0.621371

if value==1:
   Kilometers=float(input('Kilometers='))
   print('{0:.3f} miles'.format(Kilometers*n))
   
elif value==2:
   Mailes=float(input('Mailes='))
   print('{0:.3f} Kilometers'.format(Mailes/n))

else: print('Not a choice!')
