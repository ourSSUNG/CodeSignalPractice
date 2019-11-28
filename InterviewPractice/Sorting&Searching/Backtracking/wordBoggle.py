def wordBoggle(board, words):
    ans = []
    for i in range(0,len(words)):
        tmp = words[i][0]
        tmplist = list(words[i])
        tmplist.pop(0)
        for j in range(0,len(board)):
            for k in range(0,len(board[0])):
                flag = False
                if board[j][k]==tmp:
                    kboard= list(board)
                    flag = find(kboard,tmplist,[j,k])
                if flag == True:
                    ans.append(words[i])
    ans.sort()
    i = 0
    while(i+1<len(ans)):
        if ans[i] == ans[i+1]:
            ans.pop(i)
            continue
        i = i+1
    return ans
                        

    
def find(theboard,leftword,index):

    if len(leftword)==0:
        return True
    rowmax = len(theboard)
    columnmax = len(theboard[0])
    row = index[0]
    column = index[1]
    flag2 = False
    
    newboard = []
    for i in range(0,len(theboard)):
        newboard.append(list(theboard[i]))
    newboard[row][column] = "1"
    
    
    if row-1>=0 and theboard[row-1][column]==leftword[0]:
        if find(newboard,leftword[1:],[row-1,column])==True:
            flag2 = True
    if row+1<rowmax and theboard[row+1][column]==leftword[0]:
        if find(newboard,leftword[1:],[row+1,column])==True:
            flag2 = True
    if column-1>=0 and theboard[row][column-1]==leftword[0]:
        if find(newboard,leftword[1:],[row,column-1])==True:
            flag2 = True
    if column+1<columnmax and theboard[row][column+1]==leftword[0]:
        if find(newboard,leftword[1:],[row,column+1])==True:
            flag2 = True
    if row-1>=0 and column-1>=0 and theboard[row-1][column-1]==leftword[0]:
        if find(newboard,leftword[1:],[row-1,column-1])==True:
            flag2 = True
    if row-1>=0 and column+1<columnmax and theboard[row-1][column+1]==leftword[0]:
        if find(newboard,leftword[1:],[row-1,column+1])==True:
            flag2 = True
    if row+1<rowmax and column-1>=0 and theboard[row+1][column-1]==leftword[0]:
        if find(newboard,leftword[1:],[row+1,column-1])==True:
            flag2 = True
    if row+1<rowmax and column+1<columnmax and theboard[row+1][column+1]==leftword[0]:
        if find(newboard,leftword[1:],[row+1,column+1])==True:
            flag2 = True
    return flag2
