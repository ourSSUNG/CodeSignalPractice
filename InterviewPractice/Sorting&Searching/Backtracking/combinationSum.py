def combinationSum(a, sum):
    a.sort()
    i = 0
    while(i<len(a)-1):
        if a[i] == a[i+1]:
            del a[i]
            i = i-1
        i = i + 1
    maxlist = []
    for i in range(0,len(a)):
        maxlist.append(sum//a[i])
    ans1 = []
    calculater(a,sum,maxlist,0,0,ans1,[])
    if len(ans1)==0:
        return "Empty"
    realans = ""
    for i in range(0,len(ans1)):
        tmp = "("
        for j in range(0,len(ans1[i])):
            tmp = tmp + chr(ans1[i][j]+ord("0")) +" "
        tmp = tmp[:len(tmp)-1] + ")"
        realans = realans + tmp
    return realans

def calculater(a , sum , max1,trigger,currentsum,ans,tmparray):
    if trigger > len(max1)-1:
        return 0
    if currentsum + a[trigger] > sum:
        return 0
    for i in range(0,max1[trigger]+1):
        if max1[trigger]*a[trigger]-a[trigger]*i+currentsum == sum:
            ans.append(tmparray+[a[trigger]]*(max1[trigger]-i))
            continue
        calculater(a,sum,max1,trigger+1,max1[trigger]*a[trigger]-a[trigger]*i+currentsum,ans,tmparray+[a[trigger]]*(max1[trigger]-i) )
    return 0
