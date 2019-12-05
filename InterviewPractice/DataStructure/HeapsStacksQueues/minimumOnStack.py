def minimumOnStack(operations):
    ans = []
    stack = []
    minchecker = []
    for i in range(0,len(operations)):
        if operations[i] == "min":
            ans.append(minchecker[0])
        elif operations[i] == "pop":    
            num = stack.pop()
            if num == minchecker[0]:
                minchecker.pop(0)
        else:
            num = changer(operations[i][5:])
            stack.append(num)
            if len(minchecker) ==0:
                minchecker.append(num)
            else:
                if minchecker[0] > num:
                    minchecker.insert(0,num)
    return ans
    
def changer(String):
    log = 1
    n = len(String)
    sum1 = 0
    k = ord("0")
    for i in range(0,n):
        sum1 = sum1 + (ord(String[n-1-i])-k)*log
        log = log*10
    return sum1
