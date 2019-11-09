def containsCloseNums(nums, k):
    if len(nums)<2:
        return False
    flag =False
    dic = {}
    for i in range(0,len(nums)):
        if nums[i] in dic:
            dic[nums[i]] = dic[nums[i]] + 1
        else:
            dic[nums[i]] = 1
    klist = list(dic.keys())
    inchecker = False
    for i in range(0,len(klist)):
        indexlist = []
        if dic[klist[i]] > 1:
            inchecker = True
            for j in range(0,len(nums)):
                if nums[j] == klist[i]:
                    indexlist.append(j)
            for j in range(0,len(indexlist)-1):
                if indexlist[j+1]-indexlist[j] <= k:
                    flag = True
    if inchecker == False:
        return False
    
    return flag
