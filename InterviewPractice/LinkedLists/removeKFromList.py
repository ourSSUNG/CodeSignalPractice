# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    
    if l == None:
        return None
    
    while (l.next!=None):
        if l.value == k:
            
            l = l.next
        else:
            break
    if l.next == None:
        if l.value != k:
            return l
        else:
            return None
    tmp = l
    while (tmp.next!=None):
        if(tmp.next.value == k):
            tmp.next = tmp.next.next
        else:
            tmp = tmp.next
    
    if l.value != k:
        return l
    else:
        return None
            
        
