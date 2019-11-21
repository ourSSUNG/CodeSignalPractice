def decodeString(s):
    n = len(s)
    k = -1
    for i in range(0,n):
        if s[i] == "]":
            k =i
            break
    if k == -1:
        return s
    for i in range(0,k):
        if s[k-1-i] == "[":
            ks = k-1-i
            break
    tmp = s[ks+1:k]
    sum1 = 0
    log = 1
    i = 0
    while(ks-1-i>=0 and ord(s[ks-1-i])<=ord("9") ):
        sum1 = sum1 + log*(ord(s[ks-1-i])-ord("0"))
        log = log*10
        i = i + 1
    if sum1 > 0:
        s = s[:ks-i] + tmp * sum1 + s[k+1:]
    return decodeString(s)
