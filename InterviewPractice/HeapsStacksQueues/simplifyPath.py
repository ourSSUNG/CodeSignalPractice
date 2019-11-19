def simplifyPath(path):
    n = len(path)
    i = 0
    mid = []
    while(i<n):
        tmp = ""
        tmp = tmp + path[i]
        i = i + 1
        while(i<n and path[i]!="/"):
            tmp = tmp + path[i]
            i = i + 1
        if len(tmp) < 2:
            continue
        elif tmp == "/.":
            continue
        elif tmp == "/..":
            if len(mid) >0 :
                mid.pop()
            else:
                continue
        else:
            mid.append(tmp)
    ans = ""
    for i in range(0,len(mid)):
        ans = ans+ mid.pop(0)
    if ans == "":
        return "/"
    if ans[0] != "/":
        return "/" + ans
    return ans
