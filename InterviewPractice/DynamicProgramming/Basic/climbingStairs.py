def climbingStairs(n):
    if n == 1:
        return 1
    if n ==2:
        return 2
    fibo = [1,2]
    for i in range(0,n-2):
        fibo.append(fibo[i]+fibo[i+1])
    return fibo[len(fibo)-1]
    
def climbMaker(n):
    if n<=1:
        return 1
    return climbMaker(n-1) + climbMaker(n-2)
