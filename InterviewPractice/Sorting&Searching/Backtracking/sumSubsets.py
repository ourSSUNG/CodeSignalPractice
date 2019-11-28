def sumSubsets(arr, num):
    
    n = len(arr)
    check = [0]*n
    ans = []
    calculater(arr,num,0,ans,0,check)
    if len(ans)== 0:
        return [[]]
    newans = []
    for i in ans:
        if newans.count(i)<1:
            newans.append(i)
    
    return newans

def calculater(arr,num,level,ans,presum,checker):
    
    if level==len(arr):
        return 0
    tmp = arr[level]
    newch = list(checker)
    newch[level] = 1
    if presum + tmp == num:
        call = []
        for i in range(0,len(arr)):
            if newch[i]==1:
                call.append(arr[i])
        ans.append(call)
    elif presum<num:
        calculater(arr,num,level+1,ans,presum+tmp,newch)
    if presum<num:
        newch[level] = 0
        calculater(arr,num,level+1,ans,presum,newch)
    return 0
