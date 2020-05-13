#By Daliah Aljutayli
# 1 - Python program to copy all elements of one array into another array
# 2 - Python program to left rotate the elements of an array
# 3 - Python program to print the duplicate elements of an array
#-----------------------------------------------

def copyArray(array):
    #creat array2 same length
    arrayCopied = [None]*len(array)
    
    #loop to copy array 1 into second
    for copy in range(0,len(array)):
        arrayCopied[copy] = array[copy]
        
    #Diplay Elements
    print("Displaying elements of Copied Array: ",end=' ')
    for display in range(0,len(arrayCopied)):
        print(arrayCopied[display],end=' ')
#############
def rotateArray(array):
    rotateNumber = 9 #Number of rotate
    #Loop to rotate array
    for ro in range(0,rotateNumber):
        temp = array[0] # the 1st elemnt
        
        for ta in range(0,len(array)-1):
            array[ta] = array[ta+1] #Shift element
            
        array[len(array)-1] = temp #last element equal to the 1st

    #Display Element
    print('Displays Resulting Array After Rotation: ',end=' ')
    for te in range(0,len(array)):
        print(array[te],end=' ')
##############
def duplicateArray(array):
    print("Duplicate elements in given array: ",end=' ')
    #loop to search of duplicate element
    for du in range(0,len(array)):
        for pl in range(du+1,len(array)):
            if array[du] == array[pl]:
                print(array[pl],end=' ')
##############################################
                
#Initialize array
array = [1,2,3,4,5,5,4,3,3]
choice = int(input(''' Choice:
1- Copy All Elements of One Array into Another Array
2- Left Rotate The Elements of an Array
3- Print The Duplicate Elements of an Array\n'''))

if choice==1:
    copyArray(array);
elif choice ==2:
    rotateArray(array)
elif choice ==3:
    duplicateArray(array)
else: print('Sorry Not a Choice!!!')
