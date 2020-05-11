#By Daliah Aljutayli
#Python Program to Add Two Matrices
#------------------------------


matrix_X = [ [1,2,3],[4,5,6],[7,8,9]  ] # 3x3
matrix_Y = [ [10,11,12],[13,14,15],[16,17,18] ] #3x3

result = [ [0,0,0],[0,0,0],[0,0,0]  ] #3x3


for i in range(len(matrix_X)): # rows
    for j in range(len( matrix_X[0] )): #columns
        result[i][j] = matrix_X[i][j] + matrix_Y[i][j]

print('X:')
for insideX in matrix_X: # displat X matrix
    print(insideX)

print('\nY:')
for insideY in matrix_Y: # displat Y matrix
    print(insideY)

print('\nX + Y=')

for inside in result: # displat result matrix
    print(inside) 
        
    
