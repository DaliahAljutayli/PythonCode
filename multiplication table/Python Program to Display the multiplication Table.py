#By Daliah Aljuatyli
#Python Program to Display the multiplication Table

start =int (input('Multiplication Table Start From(default=1): ')or '1')
end =int (input('Multiplication Table End at(default=10): ')or '10')

number =int (input('Enter a Number: '))


for i in range (start,end+1):
    print(number,'x',i,'=',(number*i))
