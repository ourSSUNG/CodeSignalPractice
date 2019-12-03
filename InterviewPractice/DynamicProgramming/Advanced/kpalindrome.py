def kpalindrome(s, k):
    ans = [0]
    kappa(s,k,ans)
    if ans[0]==1:
        return True
    return False

def kappa(s,k,boolans):
    if len(s)<=1 and k >=0:
        boolans[0] = 1
        return 0
    if k==-1:
        return 0
    n = len(s)
    if s[0]==s[n-1]:
        kappa(s[1:n-1],k,boolans)
    else:
        kappa(s[:n-1],k-1,boolans)
        kappa(s[1:],k-1,boolans)
    return 0
