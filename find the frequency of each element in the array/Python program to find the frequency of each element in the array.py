#By Daliah Aljuatyli
#Python program to find the frequency of each element in the array
#------------------------------

arr1 = [2,4,6,6,1,8,3,2,9,6,8,3]

print('Elements of The Array are: ',end=' ')
for l in range(0,len(arr1)):
    print(arr1[l] ,end=',')


frequency = [None]*len(arr1) #array 2 same length of array 1
v = -1
arr1.sort()
for i in range(0,len(arr1)):
    c=1
    for j in range(i+1,len(arr1)):
        if arr1[i]==arr1[j]:
            c=c+1
            frequency[j] = v
        
    if frequency[i]!=v:
        frequency[i]=c

print("\nElement | Frequency")
for i in range(0, len(frequency)):
    if(frequency[i] != v):    
        print('      ',str(arr1[i]) +" | " + str(frequency[i]))
        
