def textJustification(words, l):
    ceil = l
    stack = 0
    tmp = []
    ans = []
    for i in range(0,len(words)):
        if stack + len(words[i]) <=ceil:
            stack = stack + len(words[i]) + 1
            tmp.append(words[i])
        else:
            ans.append(spliter(tmp,ceil))
            stack = len(words[i]) + 1
            tmp = [words[i]]
    last = ""
    for i in range(0,len(tmp)-1):
        last = last + tmp[i] + " "
    last = last + tmp[-1]
    while(len(last)<ceil):
        last = last + " "
    ans.append(last)
    
    return ans

def spliter(wordlist,ceil):
    length = 0
    n = len(wordlist)
    for i in range(0,n):
        length = length + len(wordlist[i])
    spacelen = ceil - length
    space = []
    if len(wordlist) == 1:
        space = [" "*spacelen]
    else:
        remainder = spacelen%(n-1)
        quotient = (spacelen - remainder)//(n-1)
        space = [" "*quotient]*(n-1)
        for i in range(0,remainder):
            space[i] = space[i] + " "
    result = ""
    for i in range(0,len(space)):
        result = result + wordlist[i]
        result = result + space[i]
    if len(wordlist) == 1:
        return result
    else:
        return result + wordlist[len(space)]
