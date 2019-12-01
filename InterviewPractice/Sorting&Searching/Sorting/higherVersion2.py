def higherVersion2(ver1, ver2):
    list1 = list(ver1)
    list2 = list(ver2)
    sub = ord("0")
    check = 0
    while(len(list1)!=0):
        log = 1
        sum1 = 0
        tmp = []
        while(len(list1)!=0 and list1[0]!="."):
            tmp.append(list1.pop(0))
        n = len(tmp)
        for i in range(0,n):
            sum1 = sum1 + log*(ord(tmp[n-i-1])-sub)
            log = log*10
        log = 1
        sum2 = 0
        tmp = []
        while( len(list2)!=0 and list2[0]!="."):
            tmp.append(list2.pop(0))
        n = len(tmp)
        for i in range(0,n):
            sum2 = sum2 + log*(ord(tmp[n-i-1])-sub)
            log = log*10
        if sum1 > sum2:
            check =1
            break
        elif sum2 > sum1:
            check = -1
            break
        if len(list1)!=0:
            list1.pop(0)
            list2.pop(0)
    return check
