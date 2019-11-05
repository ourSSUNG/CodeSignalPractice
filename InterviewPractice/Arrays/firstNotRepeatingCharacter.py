def firstNotRepeatingCharacter(s):
    howmanylist = [0]*26
    b = 0
    aski = ord('a')
    orderlist = []
    for i in range(0,len(s)):
        c = ord(s[i])
        
        howmanylist[c-aski] = howmanylist[c-aski] + 1
        if howmanylist[c-aski] == 1:
            orderlist.append(c-aski)
    for j in range(0,len(orderlist)):
        if howmanylist[orderlist[j]] == 1:
            b = 1
            return chr(orderlist[j]+aski)
            break
    return '_'
