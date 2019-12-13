def minSubstringWithAllChars(s, t):
    if len(t) == 0:
        return ""
        
    dic = {}
    indices = []
    
    for i in range(0,len(t)):
        dic[t[i]] = 0
        
    for i in range(0,len(s)):
        if s[i] in dic:
            indices.append(i)
    
    min1 = 101
    for i in range(0,len(indices)):
        tmp = endMaker(s,t,indices[i],dict(dic))
        if tmp == -1:
            break
        if tmp - indices[i] < min1:
            min1 = tmp - indices[i]
            ans = s[indices[i]:tmp+1]
        
    return ans
    
        
def endMaker(s,t,start,newdict):
    i = start
    count = 0
    while(count!=len(t)):
        if i == len(s):
            return -1
        if s[i] in newdict:
            newdict[s[i]] += 1
            if newdict[s[i]] == 1:
                count = count + 1
        i = i + 1
    return i-1
