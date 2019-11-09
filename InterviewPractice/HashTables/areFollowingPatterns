def areFollowingPatterns(strings, patterns):
    dic = {}
    i = 0
    while( i < len(strings)):
        if strings[i] in dic:
            dic[strings[i]].append(patterns[i])
        else:
            dic[strings[i]] = [patterns[i]]
        i = i+ 1
    klist = list(dic.keys())
    b = 0
    for i in range(0,len(klist)):
        for j in range(0,len(dic[klist[i]])-1):
            if dic[klist[i]][j] != dic[klist[i]][j+1]:
                b = 1
                break
                
    dic = {}
    i = 0
    while( i < len(patterns)):
        if patterns[i] in dic:
            dic[patterns[i]].append(strings[i])
        else:
            dic[patterns[i]] = [strings[i]]
        i = i+ 1
    klist = list(dic.keys())
    
    for i in range(0,len(klist)):
        for j in range(0,len(dic[klist[i]])-1):
            if dic[klist[i]][j] != dic[klist[i]][j+1]:
                b = 1
                break
    
    if b ==1:
        return False
    else:
        return True
