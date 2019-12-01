def sortedSquaredArray(array):
    n = len(array)
    min1 = array[0]*array[0]
    index = 0
    for i in range(1,len(array)):
        if array[i]*array[i] < min1:
            index = i
            min1 = array[i]*array[i]
    left = array[:index]
    left.reverse()
    right = array[index+1:]
    ans = [min1]
    while(len(left)!=0 and len(right)!=0):
        if left[0]*left[0] <= right[0]*right[0]:
            tmp = left.pop(0)
            ans.append(tmp*tmp)
        else:
            tmp = right.pop(0)
            ans.append(tmp*tmp)
    if len(left)!=0:
        while(len(left)!=0):
            tmp = left.pop(0)
            ans.append(tmp*tmp)
    elif len(right)!=0:
        while(len(right)!=0):
            tmp = right.pop(0)
            ans.append(tmp*tmp)
    return ans
