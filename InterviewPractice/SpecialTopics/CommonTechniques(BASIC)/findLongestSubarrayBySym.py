def findLongestSubarrayBySum(s, arr):
    if s==0:
        for i in range(0,len(arr)):
            if arr[i] ==0:
                return [i+1,i+1]
        return [-1]
    i = 0
    j = 0
    tmp = arr[0]
    tl = []
    while(True):
        if tmp == s:
            if j+1 < len(arr) and arr[j+1]==0:
                j = j + 1
                continue
            tl.append([i+1,j+1])
            tmp = tmp - arr[i]
            i = i + 1
            
        elif tmp > s:
            tmp = tmp - arr[i]
            i = i + 1
        elif tmp < s:
            if j+1 < len(arr):
                j = j + 1
                tmp = tmp + arr[j]
            else:
                break
    if tl == []:
        return [-1]
    min1 = 0
    minin = 0
    for i in range(0,len(tl)):
        tmp = tl[i][1]-tl[i][0]
        if tmp > min1:
            min1 = tmp
            minin = i
            
    return tl[minin]
