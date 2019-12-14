def regexMatching(pattern, test):
    if pattern[0] == "^":
        for i in range(1,len(pattern)):
            if pattern[i]!=test[i-1]:
                return False
        return True
    if pattern[-1] == "$":
        n = len(pattern)-1
        m = len(test)
        for i in range(0,n):
            if pattern[i]!=test[m-n+i]:
                return False
        return True
    n = len(pattern) -1 
    for i in range(0,len(test)-len(pattern)+1):
        if test[i] == pattern[0] and test[i+n] == pattern[n]:
            tmp = checker(pattern,test,i)
            if tmp == True:
                return True
    return False
        
    

def checker(pattern,test,ind):
    for i in range(0,len(pattern)):
        if test[ind+i]!=pattern[i]:
            return False
    return True
