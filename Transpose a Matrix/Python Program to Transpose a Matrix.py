#By Daliah Aljutayli
#Python Program to Transpose a Matrix
#-------------------------------------


matrix_X = [ [1,2],[3,4],[5,6]  ] # 3x2

result = [ [0,0,0],[0,0,0]  ] #2x3


for i in range(len(matrix_X)): # rows
    for j in range(len( matrix_X[0] )): #columns
        result[j][i] = matrix_X[i][j]

print('X:')
for insideX in matrix_X: # displat X matrix
    print(insideX)

print('\nX to X\': ')
for inside in result: # displat result matrix
    print(inside) 
        
    
