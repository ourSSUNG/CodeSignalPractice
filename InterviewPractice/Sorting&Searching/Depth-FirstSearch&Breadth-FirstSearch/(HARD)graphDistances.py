def graphDistances(g, s):
    n = len(g)
    ans = [3000]*n
    ans[s] = 0
    solved = [s]
    unsolved = []
    for i in range(0,n):
        unsolved.append(i)
    unsolved.remove(s)
    while(len(unsolved)!=0):
        jcheck = -1
        min1 = 3000
        for i in range(0,len(solved)):
            for j in range(0,len(unsolved)):
                if min1 > g[solved[i]][unsolved[j]] + ans[solved[i]] and g[solved[i]][unsolved[j]]!= -1:
                    min1 = g[solved[i]][unsolved[j]] + ans[solved[i]]
                    jcheck = unsolved[j]
        unsolved.remove(jcheck)
        solved.append(jcheck)
        ans[jcheck] = min1
    return ans
