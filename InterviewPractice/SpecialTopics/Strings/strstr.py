def strstr(s, x):
    plus = len(x)-1
    for i in range(0,len(s)-len(x)+1):
        if s[i]==x[0] and x[plus]==s[i+plus]:
            tmp = checker(s,x,i)
            if tmp == True:
                return i
    return -1
    
def checker(s,x,index):
    return s[index:index+len(x)] == x
