def mapDecoding(message):
    chrlist = list(message)
    mlist = []
    k = ord("0")
    for i in range(0,len(chrlist)):
        mlist.append(ord(chrlist[i])-k)
    if len(mlist)==0:
        return 1
    if len(mlist)==1:
        if mlist[0]==0:
            return 0
        return 1
    start = 10* mlist[0] + mlist[1]
    if start >= 10 and start <= 26:
        curr1 = 1
        curr2 = 2
    elif start < 10 or mlist[1]==0:
        return 0
    else:
        curr1 = 1
        curr2 = 1
    if start == 20 or start==10:
        curr1 = 1
        curr2 = 1
    for i in range(2,len(message)):
        if mlist[i-1]>=3:
            if mlist[i]==0:
                return 0
            else:
                curr1 = curr2
        elif mlist[i-1]==2:
            if mlist[i]==0:
                tmp = curr1
                curr1 = curr2
                curr2 = tmp
            elif mlist[i]<=6:
                tmp = curr2
                curr2 = curr1 + curr2
                curr1 = tmp
            else:
                curr1 = curr2
        elif mlist[i-1]==1:
            if mlist[i]==0:
                tmp = curr1
                curr1 = curr2
                curr2 = tmp
            else:
                tmp = curr2
                curr2 = curr2 + curr1
                curr1 = tmp
        else:
            if mlist[i]==0:
                return 0
            else:
                curr1 = curr2
    return curr2%(10**9+7)
                
