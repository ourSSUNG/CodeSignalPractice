def classifyStrings(s):
    bolist = ["a","e","i","u","o"]
    bo = 0
    mbo = 0
    con = 0
    mcon = 0
    slist = list(s)
    maxbo = 0
    maxcon = 0
    mixed = False
    
    for i in range(0 ,len(slist)):
        if slist[i] in bolist:
            bo = bo + 1
            mbo = mbo + 1
            con = 0
            mcon = 0
        elif slist[i] != "?":
            con = con + 1
            mcon = mcon + 1
            bo = 0
            mbo = 0
        else:
            mbo = mbo + 1
            mcon = mcon + 1
            if mbo==3 and bo==2 :
                con = 1
                bo = 0
            elif mcon ==5 and con ==4:
                bo = 1
                con = 0
            else:
                bo = 0
                con = 0
        if bo >=3 or con >=5:
            return "bad"
        if mbo >=3 or mcon>=5:
            mixed = True
    if mixed == True:
        return "mixed"
    return "good"
    
