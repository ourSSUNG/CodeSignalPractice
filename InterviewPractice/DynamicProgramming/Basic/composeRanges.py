def composeRanges(nums):
    if len(nums)==0:
        return []
    ans = []
    i = 0
    check = False
    nums.append(nums[0])
    while(i<len(nums)-1):
        if check == False:
            if nums[i]+1 != nums[i+1]:
                ans.append(str(nums[i]))
                i = i+1
                continue
            else:
                tmp = nums[i]
                check = True
                i = i+1
                continue
        else:
            if nums[i]+1 != nums[i+1]:
                ans.append(str(tmp)+"->"+str(nums[i]))
                i = i+1
                check = False
            else:
                i = i+1
    return ans
