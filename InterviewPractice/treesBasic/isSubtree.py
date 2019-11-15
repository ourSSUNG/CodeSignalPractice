#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isSubtree(t1, t2):
    if t2 == None:
        return True
    if t1 == None:
        return False
    nod1 = []
    str1 = []
    nod2 = []
    str2 = []
    sequenceMaker(t1,nod1,str1)
    sequenceMaker(t2,nod2,str2)
    flag = False
    for i in range(0,len(nod1)-len(nod2)+1):
        if nod1[i] != nod2[0]:
            continue
        flag2 = True
        for j in range(0,len(nod2)):
            if nod1[i+j] != nod2[j]:
                flag2 = False
                break
            if str1[i+j] != str2[j]:
                flag2 = False
                break
        if flag2==True:
            flag = True
            break
    return flag
    
def sequenceMaker(t,nodelist,structurelist):
    if t.left==None:
        if t.right == None:
            structurelist.append(1)
            nodelist.append(t.value)
            return nodelist
        else:
            structurelist.append(2)
            nodelist.append(t.value)
            sequenceMaker(t.right,nodelist,structurelist)
            return nodelist
    else:
        if t.right == None:
            
            sequenceMaker(t.left,nodelist,structurelist)
            structurelist.append(3)
            nodelist.append(t.value)
            return nodelist
        else:
            
            sequenceMaker(t.left,nodelist,structurelist)
            structurelist.append(4)
            nodelist.append(t.value)
            sequenceMaker(t.right,nodelist,structurelist)
            return nodelist
        
