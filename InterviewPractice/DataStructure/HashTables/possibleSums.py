def possibleSums(coins, quantity):
    
    dic = {}
    dic[0] = 1
    
    for i in range(0,len(coins)):
        klist = list(dic.keys())
        for j in range(1,quantity[i]+1):
            
            for k in range(0,len(klist)):
                if j*coins[i] + klist[k] in dic:
                    a=0
                else:
                    dic[j*coins[i] + klist[k]] = 1
    
    
    return len(list(dic.keys()))-1
