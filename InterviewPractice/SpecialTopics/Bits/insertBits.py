def insertBits(n, a, b, k):
    bitlist = []
    log = 2
    while(n!=0):
        tmp = n%log
        bitlist.append(tmp*2//log)
        n = n - tmp
        log = log * 2
    for i in range(0,b+1):
        bitlist.append(0)
    newbit = []
    if k==0:
        newbit = [0]
    log = 2
    while(k!=0):
        tmp = k%log
        newbit.append(tmp*2//log)
        k = k - tmp
        log = log * 2
    while(len(newbit)<b-a+1):
        newbit.append(0)
    
    bitlist.reverse()
    
    m = len(bitlist)
    for i in range(0,len(newbit)):
        bitlist[m-a-i-1] = newbit[i]
    log = 1
    ans = 0
    bitlist.reverse()
    for i in range(0,len(bitlist)):
        ans = ans + log* bitlist[i]
        log = log*2
    return ans
