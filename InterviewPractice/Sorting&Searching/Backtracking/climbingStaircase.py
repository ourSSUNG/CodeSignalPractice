def climbingStaircase(n, k):
    ans = []
    stepfirst = []
    caseDivider(n,k,0,stepfirst,ans)
    return ans

def caseDivider(n,k,cursum,steps,ans):
    
    if cursum == n:
        ans.append(steps)
        return 0
    elif cursum>n:
        return 0
    
    for i in range(0,k):
        tmp = i+1
        caseDivider(n,k,cursum+tmp,steps+[tmp],ans)
    return 0
