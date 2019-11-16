#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def restoreBinaryTree(inorder, preorder):
    return (dwgTreeMaker(inorder,preorder))


    
def dwgTreeMaker(inorder, preorder):
    if inorder == []:
        return None
    t = Tree(preorder[0])
    num = 0
    for i in range(0,len(inorder)):
        if inorder[i] == preorder[0]:
            num = i
            break
    t.left = dwgTreeMaker(inorder[:num],preorder[1:num+1])
    t.right = dwgTreeMaker(inorder[num+1:],preorder[num+1:])
        
    return t
