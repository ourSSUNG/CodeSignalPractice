#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def digitTreeSum(t):
    return treeSumCalculate(t,[])

    
    
def treeSumCalculate(t,codelist):
    k = list(codelist)
    k.append(t.value)
    if t.left == None and t.right == None:
        log = 1
        sum1 = 0
        n = len(k)
        for i in range(0,n):
            sum1 = sum1 + log*k[n-i-1]
            log = log*10
        return sum1
    if t.left == None:
        return treeSumCalculate(t.right,k)
    elif t.right == None:
        return treeSumCalculate(t.left,k)
    else:
        return treeSumCalculate(t.right,k) + treeSumCalculate(t.left,k)
