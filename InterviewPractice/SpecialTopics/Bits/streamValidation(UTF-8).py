def streamValidation(stream):
    stack = 0
    now = False
    for i in range(0,len(stream)):
        n = stream[i]
        if stack >0:
            if n>=128 and n<= 191:
                stack = stack - 1
                continue
            else:
                return False
        
        if n <=127:
            stack = 0
            continue
        else:
            if n>=192 and n<= 223:
                stack = 1
                continue
            elif n>= 224 and n<= 239:
                stack = 2
                continue
            elif n>= 240 and n<= 247:
                stack = 3
                continue
            else:
                return False
    if stack!=0:
        return False
    return True
