def productExceptSelf(nums, m):
    a = 0
    b = 1
    for i in range(0,len(nums)):
        a = a*nums[i] + b
        b = b*nums[i]
    return a%mv
