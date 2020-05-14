#By Daliah Aljutayli
#Python program to print the number of elements present in an array
#Python program to print the sum of all elements in an array
#Python program to right rotate the elements of an array
#Python program to sort the elements of an array in ascending order
#Python program to sort the elements of an array in descending order
#----------------------------------------------

arr = [1,3,5,7,9,11,2,4,6,8]

print('The Elements of The Array= ',end='')
for show in range(0,len(arr)):
    print(arr[show],end=' ')

print('\nThe Number of Elements Present in an Array is= ',len(arr),end='')
#__________________________
print('\nThe SUM of All Elements in an Array is= ',end='')
temp=0
for s in range(0,len(arr)):
    temp+=arr[s]
print(temp,end='')
#__________________________
print('\nRight Rotate The elements of an Array as= ',end='')
rotateNumber = 3 #Number of rotate
for ro in range(0,rotateNumber):
    last = arr[len(arr)-1]
    
    for ta in range(len(arr)-1,-1,-1):
        arr[ta] = arr[ta-1] #Shift element
        
    arr[0] = last #last element equal to the 1st

#Display Element
for te in range(0,len(arr)):
    print(arr[te],end='')
#_________________________
print('\nSort The Elements in Ascending Order = ',sorted(arr))
print('Sort The Elements in Descending Order  = ',sorted(arr,reverse=True))
