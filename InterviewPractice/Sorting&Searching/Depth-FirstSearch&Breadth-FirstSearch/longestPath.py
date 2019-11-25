def longestPath(fileSystem):
    n = len(fileSystem)
    k =0
    tmp = ""
    stack = []
    count = 0
    ans = 0
    while(k<n):
        if fileSystem[k]=="\t":
            count = count + 1
            k = k+1
            continue
        elif fileSystem[k]!="\f":
            tmp = tmp + fileSystem[k]
            k = k+1
            continue
        while(count<len(stack)):
            stack.pop(0)
        count = 0
        flag = False
        for i in range(1, len(tmp)-1):
            if tmp[i] == ".":
                flag = True
                break
        if flag == True:
            tmpmax = 0
            for i in range(0,len(stack)):
                tmpmax = tmpmax + len(stack[i])
            tmpmax = tmpmax + len(tmp) + len(stack)
            if tmpmax > ans:
                ans = tmpmax
        else:
            stack.insert(0,tmp)
        tmp = ""
        k = k+1
    while(count<len(stack)):
        stack.pop(0)
    flag = False
    for i in range(1, len(tmp)-1):
        if tmp[i] == ".":
            flag = True
            break
    if flag == True:
        tmpmax = 0
        for i in range(0,len(stack)):
            tmpmax = tmpmax + len(stack[i])
        tmpmax = tmpmax + len(tmp) + len(stack)
        if tmpmax > ans:
            ans = tmpmax
    
    return ans
