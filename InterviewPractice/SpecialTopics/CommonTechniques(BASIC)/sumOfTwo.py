def sumOfTwo(a, b, v):
    a.sort()
    b.sort()
    b.reverse()
    i = 0
    j = 0
    alen = len(a)
    blen = len(b)
    while(i<alen and j<blen):
        if a[i] + b[j] > v:
            j = j + 1
        elif a[i] + b[j] < v:
            i = i + 1
        else:
            return True
    
    return False
