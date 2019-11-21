def nextLarger(a):
    stack = []
    n = len(a)
    ans = []
    ans.append(-1)
    stack.append(a[n-1])
    maxnum = stack[0]
    for i in range(2,n+1):
        while(len(stack)!=0):
            if stack[len(stack)-1] <= a[n-i]:
                stack.pop()
            else:
                ans.append(stack[len(stack)-1])
                stack.append(a[n-i])
                break
        if len(stack) ==0:
            stack.append(a[n-i])
            ans.append(-1)
    ans.reverse()
    return ans
