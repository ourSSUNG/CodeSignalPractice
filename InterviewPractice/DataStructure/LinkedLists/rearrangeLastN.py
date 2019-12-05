# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def rearrangeLastN(l, n):
    if l == None or n == 0:
        return l
    tmp1 = l
    i = 0
    while(tmp1.next!=None):
        tmp1=tmp1.next
        i=i+1
    if i+1 == n:
        return l
    end = tmp1
    j = i+1 - n
    i = 0
    tmp1 = l
    while (i<j-1):
        tmp1 = tmp1.next
        i = i + 1
    tmp2 = tmp1.next
    tmp1.next = None
    end.next = l
    return tmp2
