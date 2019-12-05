def groupingDishes(dishes):
    dic = {}
    i = 0
    while(i<len(dishes)):
        j = 1
        while(j<len(dishes[i])):
            if dishes[i][j] in dic:
                dic[dishes[i][j]].append(dishes[i][0])
            else:
                dic[dishes[i][j]] = [dishes[i][0]]
            j=j+1
        i = i + 1
    klist = list(dic.keys())
    klist.sort()
    ans = []
    
    
    for i in range(0,len(klist)):
        if len(dic[klist[i]]) > 1:
            dic[klist[i]].sort()
            ans.append([klist[i]]+dic[klist[i]])
            
            
            
    return ans
              
