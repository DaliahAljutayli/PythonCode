#By Daliah Aljuatyli
#Python program to print the elements of an array in reverse order
#Python program to print the elements of an array present on even position
#Python program to print the elements of an array present on odd position
#Python program to print the largest element in an array
#--------------------------------

arr = [100,2,33,4,5,11,6,7,15,0,1]


print('Elements of The Array are= ',end='')
for i in range(0,len(arr)):    
    print(arr[i] ,end=' ')

print('\n\nElements Present on EVEN Position are= ',end='')
for e in range(1,len(arr),2):#increment by 2 , start from 1
    print(arr[e] ,end=' ')

print('\n\nElements Present on ODD Position are= ',end='')
for o in range(0,len(arr),2):#increment by 2,  start from 0
    print(arr[o] ,end=' ')

print('\n\nThe Largest Element in an Array = ',end='')
temp=arr[0]
for L in range(0,len(arr)):
    if arr[L]>temp:
        temp= arr[L] #the largest inside temp
print(temp,end='')

#______________________________________________
print('\n\nElements in Reverse Order Using for Loop = ',end='')
for f in range(len(arr)-1,-1,-1):#start from last element ,decrement by -1
    print(arr[f] ,end=' ')
    
arr.reverse()
print('\n\nElements in Reverse Order Using reverse()= ',end='')
for r in range(0,len(arr)):    
    print(arr[r] ,end=',')


