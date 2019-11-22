#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def largestValuesInTreeRows(t):
    if t == None:
        return []
    nodelist = [t]
    level = []
    ans = []
    while(len(nodelist)!=0):
        level = []
        newnode = []
        for i in range(0,len(nodelist)):
            level.append(nodelist[i].value)
            if nodelist[i].left!=None:
                newnode.append(nodelist[i].left)
            if nodelist[i].right!=None:
                newnode.append(nodelist[i].right)
        nodelist = newnode
        maxvalue = level[0]
        for i in range(1,len(level)):
            if maxvalue < level[i]:
                maxvalue = level[i]
        ans.append(maxvalue)
    return ans
