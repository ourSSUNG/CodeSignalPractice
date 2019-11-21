#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def traverseTree(t):
    if t == None:
        return []
    ans = []
    nodes = [t]
    values = []
    while(len(nodes)!=0):
        values = []
        for i in range(0, len(nodes)):
            values.append(nodes[i].value)
        
        ans = ans + values
        newnodes = []
        for i in range(0,len(nodes)):
            if nodes[i].left != None:
                newnodes.append(nodes[i].left)
            if nodes[i].right != None:
                newnodes.append(nodes[i].right)
        nodes = newnodes
    return ans
                
