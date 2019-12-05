def countClouds(skyMap):
    rowmax = len(skyMap)-1
    if rowmax == -1:
        return 0
    columnmax = len(skyMap[0])-1
    stack = 0
    for i in range(0,rowmax+1):
        for j in range(0,columnmax+1):
            if skyMap[i][j] == '1':
                stack = stack +1
                Eraser(skyMap,[i,j],rowmax,columnmax)
    return stack

def Eraser(S,coordinate,rowmax,columnmax):
    row = coordinate[0] 
    column = coordinate[1]
    if S[row][column] == '0':
        return 0
    S[row][column] = '0'
    if row != 0:
        Eraser(S,[row-1,column],rowmax,columnmax)
    if row != rowmax:
        Eraser(S,[row+1,column],rowmax,columnmax)
    if column != 0:
        Eraser(S,[row,column-1],rowmax,columnmax)
    if column != columnmax:
        Eraser(S,[row,column+1],rowmax,columnmax)
    return 0
    
