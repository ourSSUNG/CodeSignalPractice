def firstDuplicate(a):
    b = 0
    n = len(a)
    seen = [0] * (n + 1)
    for i in range (0 , n):
        if seen[a[i]] == 1:
            b = 1
            break
        seen[a[i]] = 1
    if b == 0:
        return -1
    else:
        return a[i]
        
