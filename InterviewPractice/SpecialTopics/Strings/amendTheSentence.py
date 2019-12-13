def amendTheSentence(s):
    if ord(s[0]) < 96:
        ans = chr(ord(s[0]) + 32)
    else:
        ans = s[0]
    
    for i in range(1,len(s)):
        if ord(s[i]) < 96:
            ans = ans + " " + chr(ord(s[i]) + 32)
        else:
            ans= ans + s[i]
    return ans
