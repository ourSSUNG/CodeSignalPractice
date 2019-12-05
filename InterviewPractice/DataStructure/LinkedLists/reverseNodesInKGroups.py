# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseNodesInKGroups(l, k):
    if k == 1 or k == 0:
        return l
    tmp1 = l
    for i in range(0,k-1):
        tmp1= tmp1.next
    start = tmp1
    areastart = l
    areaend = ListNode(0)
    b=0
    while(True):
        checker = areastart
        for i in range(0,k):
            if checker == None:
                b = 1
                areaend.next = areastart
                break
            checker=checker.next
        if b == 1:
            break
        tmp1 = areastart
        tmp2 = areastart.next
        for j in range(0,k-1):
            tmp3 = tmp2.next
            tmp2.next = tmp1
            tmp1 = tmp2
            tmp2 = tmp3
        areaend.next = tmp1
        areaend = areastart
        areastart = tmp2
        
    return start
        
