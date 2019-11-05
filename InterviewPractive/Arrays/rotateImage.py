def rotateImage(a):
    n = len(a[0])
    tmp = 0
    for i in range (0,n//2):
        for j in range (0+i,n-1-i):
            tmp = a[i][j]
            a[i][j] = a[n-j-1][i]
            a[n-j-1][i] = a[n-i-1][n-j-1]
            a[n-i-1][n-j-1] = a[j][n-i-1]
            a[j][n-i-1] = tmp
    return a
