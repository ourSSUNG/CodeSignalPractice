def fillingBlocks(n):
    return blockMaker(n)
    
def blockMaker(n):
    if n==2:
        return 5
    if n==1:
        return 1
    if n==0:
        return 0
    sum1 = 0
    sum1 = sum1 + blockMaker(n-1)
    sum1 = sum1 + 4*blockMaker(n-2)
    for i in range(1,n-2):
        sum1 = sum1 + 2*blockMaker(n-2-i)
    sum1 = sum1 + 2
    k = n%2
    if k==1:
        for i in range(1,n//2):
            sum1 = sum1 + blockMaker(n-2-i*2)
    else:
        for i in range(2,n//2):
            sum1 = sum1 + blockMaker(n-i*2)
        sum1 = sum1 + 1
    return sum1
