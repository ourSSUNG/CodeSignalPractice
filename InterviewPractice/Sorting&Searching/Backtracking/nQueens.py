def nQueens(n):
    chess = [[0]*n]*n
    ans = []
    tmp1 = []
    queenMaker(n,chess,0,tmp1,ans)
    return ans

def queenMaker(n,thechess,level,tmp,ans):
    if level==n:
        ans.append(tmp)
        return 0
    for i in range(0,n):
        if thechess[level][i]==0:
            newchess = []
            for j in range(0,n):
                newchess.append(list(thechess[j]))
            drawer(n,newchess,[level,i])
            queenMaker(n,newchess,level+1,tmp+[i+1],ans)
    return 0
    
def drawer(n,plate,index):
    row=index[0]
    column = index[1]
    i = row
    while(i>=0):
        plate[i][column] = 1
        i = i-1
    i = row
    while(i<n):
        plate[i][column] = 1
        i = i+1
    i = column
    while(i>=0):
        plate[row][i] = 1
        i = i-1
    i = column
    while(i<n):
        plate[row][i] = 1
        i = i+1
    i = row
    j = column
    while(i>=0 and j>=0):
        plate[i][j] = 1
        i = i-1
        j = j-1
    i = row
    j = column
    while(i>=0 and j<n):
        plate[i][j] = 1
        i = i-1
        j = j+1
    i = row
    j = column
    while(i<n and j>=0):
        plate[i][j] = 1
        i = i+1
        j = j-1
    i = row
    j = column
    while(i<n and j<n):
        plate[i][j] = 1
        i = i+1
        j = j+1
    return 0
