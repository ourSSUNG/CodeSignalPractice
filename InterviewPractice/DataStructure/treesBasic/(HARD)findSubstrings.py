class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def findSubstrings(words, parts):
    thetree = treeMaker7(parts)
    for i in range(0,len(words)):
        for m in range(0,5):
            if len(words[i])<5-m:
                continue
            log = 1
            sum1 = 0
            for j in range(0,5-m):
                sum1 = sum1 + log*(ord(words[i][j])-64)
                log = log*60
            log = log/60
            if BTSearch(thetree,sum1)==True:
                words[i] = "[" + words[i][:5-m] + "]" + words[i][5-m:]
                break
            flag = False
            for j in range(1,len(words[i])-4+m):
                sum1 = sum1-(ord(words[i][j-1])-64)
                sum1 = sum1/60
                sum1 = sum1 + log*(ord(words[i][j+4-m])-64)
                flag = False
                if BTSearch(thetree,sum1)==True:
                    words[i] = words[i][:j] + "[" + words[i][j:j+5-m] + "]" + words[i][j+5-m:]
                    flag = True
                    break
            if flag == True:
                break
    return words
        
            
def treeApend(t,num):
    tmp = t
    while(True):
        if tmp.value > num:
            if tmp.left == None:
                tmp.left = Tree(num)
                break
            else:
                tmp = tmp.left
                continue
        elif tmp.value < num:
            if tmp.right == None:
                tmp.right = Tree(num)
                break
            else:
                tmp = tmp.right
                continue
        else:
            break
    return t

def BTSearch(t,key):
    tmp1 = t
    while(tmp1!=None):
        if tmp1.value > key:
            tmp1 = tmp1.left
        elif tmp1.value < key:
            tmp1 = tmp1.right
        else:
            return True
    return False

def treeMaker7(thelist):
    if len(thelist) == 0:
        return None
    len1 = len(thelist[0])
    log = 1
    sum1 = 0
    for i in range(0,len1):
        sum1 = sum1 + log*(ord(thelist[0][i])-64)
        log = log*60
    
    root = Tree(sum1)
    for i in range(1,len(thelist)):
        len1 = len(thelist[i])
        log = 1
        sum1 = 0
        for j in range(0,len1):
            sum1 = sum1 + log*(ord(thelist[i][j])-64)
            log = log*60
        treeApend(root,sum1)
    return root
    
