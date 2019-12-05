def swapLexOrder(str, pairs):
    
    
    str2 = list(str)
    dic= {}
    j = 0
    
    for i in range(0,len(pairs)):
        b = 0
        tmp = pairs[i]
        
        if tmp[1] in dic:
            b = b + 1
            num1 = dic[tmp[1]]
        if tmp[0] in dic:
            b = b + 2
            num2 = dic[tmp[0]]
        if b==0:
            dic[tmp[0]] = j
            dic[tmp[1]] = j
            j += 1
        elif b == 1:
            dic[tmp[0]] = dic[tmp[1]]
        elif b == 2:
            dic[tmp[1]] = dic[tmp[0]]
        else:
            tuplist = list(dic.items())
            for k in range(0,len(tuplist)):
                if tuplist[k][1] == num1:
                    dic[tuplist[k][0]] = num2
            
    klist = list(dic.keys())
    i = 0
    diclist = [[] for i in range(0,j)]
    
    for i in range(0,len(klist)):
        diclist[dic[klist[i]]].append(klist[i])
    
    
    for i in range(0,j):    
        klist = list(diclist[i])
        klist.sort()
        charlist = []
        for k in range(0,len(klist)):
            charlist.append(str[klist[k]-1])
        charlist.sort()
        charlist.reverse()
        
        for k in range(0,len(klist)):
            str2[klist[k]-1] = charlist[k]
            
    return ''.join(str2)

