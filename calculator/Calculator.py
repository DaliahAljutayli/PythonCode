#Calculator by Daliah Aljutayli
#Calculation between two numbers
#----------------------------------------------
def Arithmetic_Operators(choice):
   num1 = int( input("First  Number= ") )
   num2 = int (input("Second Number= "))
   if choice == 1:
      print(num1+num2)
   elif choice == 2:
      print(num1-num2)      
   elif choice == 3:
      print(num1*num2)      
   elif choice == 4:
      print(num1/num2)      
   elif choice == 5:
      print(num1%num2)      
   elif choice == 6:
      print(num1**num2)
   else:
      print('Nothing to print!')    
#---------------------------------------------
start=input('Enter: y to Start \nEnter: n to Finish!\n')
while start != 'n':
   choice = input('''1- Addition
2- Subtraction
3- Multiplication
4- Division
5- Modulus
6- Exponentiation
7- Floor division
n- Exit
''') #input take str
   
# Check if number where choice not equal to n which is Finish
   if choice != 'n':
      choice=int(choice) #from str into int
      Arithmetic_Operators(choice)
   else:
      print('Exit!!!')
      break
