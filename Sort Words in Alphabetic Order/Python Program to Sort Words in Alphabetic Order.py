#By Daliah Aljutayli
#Python Program to Sort Words in Alphabetic Order
#-------------------------------------


string = input('Enter a String: ')

# Split words into list then sort them!
W = string.split() 
W.sort()

for i in W:
    print(i)
    
print('\n\nIn Reverse:')
W.reverse()
for c in W:
    print(c)
