#By Daliah Aljutayli
#Python program to solve quadratic equation
#Help : mathsisfun.com and mathbitsnotebook.com

import cmath

print("\nEnter the coefficients for the Ax2 + Bx + C = 0")
a = float(input('A= '))
b = float(input('B= '))
c = float(input('C= '))

if a !=0:
   discriminant=(b**2)-(4*a*c)
   x1=(-b+cmath.sqrt(discriminant)) /(2*a)
   x2=(-b-cmath.sqrt(discriminant)) /(2*a)

   if discriminant>0:
      print('Positive Roots:Two Real Roots: ',x1.real,'and',x2.real)
   elif discriminant<0:
      print('Negative Roots:Two Complex Root: {0:.1f}'.format(x1),', ','{0:.1f}'.format(x2) )
   else:
      print('Zero Root:One Real Root: ',x1.real)

else: #a is 0
   print('Not a quadratic equation. \'A\' shouldn\'t be zero!')
