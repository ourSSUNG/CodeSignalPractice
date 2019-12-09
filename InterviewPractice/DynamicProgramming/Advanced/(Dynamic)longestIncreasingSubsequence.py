def paintHouses(cost):
    global dina
    dina = [cost[0]]
    n = len (cost)
    for i in range(1,n):
        paintMaker(cost,i)
    ans = list(dina[n-1])
    ans.sort()
    return ans[0]
    
def paintMaker(cost,level):
    newlev= [0,0,0]
    if dina[level-1][1]<dina[level-1][2]:
        newlev[0] = dina[level-1][1] + cost[level][0]
    else:
        newlev[0] = dina[level-1][2] + cost[level][0]
    if dina[level-1][0]<dina[level-1][2]:
        newlev[1] = dina[level-1][0] + cost[level][1]
    else:
        newlev[1] = dina[level-1][2] + cost[level][1]
    if dina[level-1][0]<dina[level-1][1]:
        newlev[2] = dina[level-1][0] + cost[level][2]
    else:
        newlev[2] = dina[level-1][1] + cost[level][2]
    dina.append(newlev)
    return 0
