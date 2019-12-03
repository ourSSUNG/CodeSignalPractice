def houseRobber(nums):
    if len(nums)==0:
        return 0
    if len(nums)==1:
        return nums[0]
    curr1 = nums[0]
    if nums[0] >=nums[1]:
        check = False
        curr2 = curr1
    else:
        check = True
        curr2 = nums[1]
    for i in range(2,len(nums)):
        if check == False:
            curr1 =curr2
            curr2 = curr2 + nums[i]
            check = True
            continue
        if curr1 + nums[i] <= curr2:
            curr1 = curr2
            check = False
        else:
            tmp = curr1
            curr1 = curr2
            curr2 = tmp + nums[i]
    
    if curr1 < curr2:
        return curr2
    else:
        return curr1
    
