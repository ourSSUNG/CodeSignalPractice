def maximalSquare(matrix):
    
    if matrix == []:
        return 0
    
    
    best = 0
    rowmax = len(matrix)
    columnmax = len(matrix[0])
    
    
    i = 0
    while(True):
        if i >= rowmax - best:
            break
        j = 0
        print(i)
        while(True):
            if j >= columnmax - best or i >= rowmax - best:
                break
            
            trigger = True
            for k in range(0,best+1):
                if matrix[i][j+k] != "1":
                    trigger = False
            if trigger == True:
                if squCheck(matrix,i,j,best+1) == True:
                    
                    best = best + 1
                    j = 0
                    continue
            j = j + 1
        i = i + 1
        
    return best * best
def squCheck(matrix,rin,cin,maxn):

    for i in range(rin+1,rin+maxn):
        for j in range(cin,cin+maxn):
            if matrix[i][j] != "1":
                return False
    return True
    
