#By Daliah Aljutayli
#Python Program to Make a Simple Calculator
#------------------------------------------

def summ(x,y):print(num1+num2)
def sub(x,y):print(num1-num2)
def mult(x,y):print(num1*num2)
def div(x,y):
   if y!=0:print(num1/num2)
   else:print('Can\'t divide by ZERO')
def mof(x,y):print(num1%num2)
def exp(x,y):print(num1**num2)
def floor(x,y):print(num1//num2)    
#---------------------------------------------
start=input('Enter any letter to Start \nEnter: n to Finish!\n')
while start != 'n':
   choice = input('''1- Addition
2- Subtraction
3- Multiplication
4- Division
5- Modulus
6- Exponentiation
7- Floor division
n- Exit ''') #input take str
   
# Check if number where choice not equal to n which is Finish
   if choice != 'n':
      choice=int(choice) #from str into int
      num1 = int( input("First  Number= ") )
      num2 = int (input("Second Number= "))
      if choice == 1:summ(num1,num2)
      elif choice == 2:sub(num1,num2)      
      elif choice == 3:mult(num1,num2)      
      elif choice == 4:div(num1,num2)      
      elif choice == 5:Mod(num1,num2)      
      elif choice == 6:exp(num1,num2)
      elif choice == 7:floor(num1,num2)
      else:print('Nothing to print!')  
   else:
      print('Exit!!!')
      break




