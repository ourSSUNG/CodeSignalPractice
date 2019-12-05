def leftGreater(a):
    ans = [-1]
    n = len(a)
    stack = [[a[0],0]]
    for i in range(1,n):
        tmp = a[i]
        check = i
        while(len(stack)!=0):
            if stack[0][0] <= tmp:
                stack.pop(0)
            else:
                check = stack[0][1]
                break
        if check == i:
            ans.append(-1)
            stack.insert(0,[a[i],i])
        else:
            ans.append(stack[0][1])
            stack.insert(0,[a[i],i])
    return ans

def rightGreater(a):
    a.reverse()
    ans = [-1]
    n = len(a)
    stack = [[a[0],0]]
    for i in range(1,n):
        tmp = a[i]
        check = i
        while(len(stack)!=0):
            if stack[0][0] <= tmp:
                stack.pop(0)
            else:
                check = stack[0][1]
                break
        if check == i:
            ans.append(-1)
            stack.insert(0,[a[i],i])
        else:
            ans.append(n-1-stack[0][1])
            stack.insert(0,[a[i],i])
    ans.reverse()
    return ans
        
def nearestGreater(a):
    left = leftGreater(a)
    right = rightGreater(a)
    n = len(a)
    ans = []
    for i in range(0,n):
        if left[i] == -1:
            ans.append(right[i])
            continue
        if right[i] == -1:
            ans.append(left[i])
            continue
        
        if i - left[i] <= right[i] -i:
            ans.append(left[i])
        else:
            ans.append(right[i])
    return ans
