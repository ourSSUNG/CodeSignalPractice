def sortByString(s, t):
    s = list(s)
    t = list(t)
    ans = ""
    for i in range(0,len(t)):
        n = t[i]
        count = 0
        j = 0
        while(j<len(s)):
            if s[j]==n:
                count = count + 1
                s.pop(j)
                j = j -1
            j = j + 1
        ans = ans + n*count
    return ans
