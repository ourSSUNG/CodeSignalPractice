def isCryptSolution(crypt, solution):
    string1 = crypt[0]
    string2 = crypt[1]
    string3 = crypt[2]
    asciinum = ord("0")
    i = 0
    log = 1
    sum1 = 0
    tmp = 0
    b = 0
    while i < len(string1):
        for j in range(0,len(solution)):
            if string1[len(string1)-1-i] == solution[j][0]:
                tmp = ord(solution[j][1]) - asciinum
                break
        sum1 = sum1 + log*tmp
        i = i + 1
        log = log*10
        if i == len(string1) and tmp == 0 and i != 1:
            b =1
    
    log = 1
    i = 0
    sum2 = 0
    while i < len(string2):
        for j in range(0,len(solution)):
            if string2[len(string2)-1-i] == solution[j][0]:
                tmp = ord(solution[j][1]) - asciinum
                break
        sum2 = sum2 + log*tmp
        i = i + 1
        log = log*10
        if i == len(string2) and tmp == 0 and i != 1:
            b=1
    
    log = 1
    i = 0
    sum3 = 0
    while i < len(string3):
        for j in range(0,len(solution)):
            if string3[len(string3)-1-i] == solution[j][0]:
                tmp = ord(solution[j][1]) - asciinum
                break
        sum3 = sum3 + log*tmp
        i = i + 1
        log = log*10
        if i == len(string3) and tmp == 0 and i != 1:
            b=1
        
    
    if sum1 + sum2 == sum3 and b == 0:
        return True
    else:
        return False
