#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def deleteFromBST(t, queries):
    for i in range(0, len(queries)):
        if t == None:
            return None
        t = BTS(t,queries[i])
    return t

    
def BTS(t,thenum):
    if t.value == thenum:
        if t.left == None:
            return t.right
        else:
            tmpmother = t
            start = t.left
            while(start.right!=None):
                tmpmother = start
                start = start.right
            if tmpmother.value == thenum:
                start.right = tmpmother.right
                return start
            if start.left == None:
                tmpmother.right = None
                start.right = t.right
                start.left = t.left
                return start
            else:
                tmpmother.right = start.left
                start.right = t.right
                start.left = t.left
                return start
    mother = find(t,thenum)
    sidechecker= 0
    if mother == None:
        return t
    if mother.left == None:
        start = mother.right
        sidechecker = 1
    elif mother.right == None:
        start = mother.left
        sidechecker = 2
    else:
        if mother.right.value == thenum:
            start = mother.right
            sidechecker = 1
        else:
            start = mother.left 
            sidechecker = 2
    if start.left == None:
        if sidechecker == 1:
            mother.right = start.right
        else:
            mother.left = start.right
    else:
        tmpmother = start
        start = start.left
        while(start.right!=None):
            tmpmother = start
            start = start.right
        if tmpmother.value == thenum:
            if sidechecker == 1:
                mother.right = start
                start.right = tmpmother.right
                return t
            else:
                mother.left = start
                start.right = tmpmother.right
                return t
        if start.left == None:
            tmpmother.right = None
            if sidechecker ==1:
                tmp2 = mother.right
                mother.right = start
                start.right = tmp2.right
                start.left = tmp2.left
            else:
                tmp2 = mother.left
                mother.left = start
                start.right = tmp2.right
                start.left = tmp2.left
        else:
            tmpmother.right = start.left
            if sidechecker ==1:
                tmp2 = mother.right
                mother.right = start
                start.right = tmp2.right
                start.left = tmp2.left
            else:
                tmp2 = mother.left
                mother.left = start
                start.right = tmp2.right
                start.left = tmp2.left
    return t
            

def find(t,thenum):
    if t.value > thenum:
        tmp = t.left
    else:
        tmp = t.right
    mother = t
    while(tmp!=None):
        if tmp.value > thenum:
            mother = tmp
            tmp = tmp.left
        elif tmp.value < thenum:
            mother = tmp
            tmp = tmp.right
        else:
            break
    if tmp != None:
        return mother
    else:
        return None
