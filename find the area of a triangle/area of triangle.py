#Find area of triangle by Daliah Aljutayli
#Formula from mathsisfun.com:

import math
start = input('To star press s\nTo Finish press f!   ')

while start !='f':
   print('\nFind Area of Triangle:')
   enter=input('''
   1-Knowing Base and Height
   2-Knowing Three Sides
   3-Using One Side of an Equilateral Triangle
   f- for Finish!!
   ''')
   if enter == '1':
      #Where b is Base and h is Height.
      base = float(input('Enter the base= '))
      height =float( input('Enter the height= '))
      area =(1/2)*(base*height)
      print("{0:.2f}".format(area))

   elif enter == '2':
      side1 =float(input('Enter Side 1= '))
      side2 =float( input('Enter Side 2= '))
      side3 =float( input('Enter Side 3= '))
      SIDE = (side1+side2+side3)/2
      area =math.sqrt(SIDE*(SIDE-side1)*(SIDE-side2)*(SIDE-side3))
      print("{0:.2f}".format(area))
   
   elif enter == '3':
      side = float(input('Enter The Side= '))
      area =(math.pow(side,2))*((math.sqrt(3))/4)
      print("{0:.2f}".format(area))
   else:break
      
print('Exit !!')
