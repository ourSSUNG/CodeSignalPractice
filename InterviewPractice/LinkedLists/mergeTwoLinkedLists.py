# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    pointer1=l1
    pointer2=l2
    b = 0
    if l1.value>l2.value:
        b = 1
        tmp = l2
        pointer2 = pointer2.next    
    else:
        tmp = l1
        pointer1 = pointer1.next
        
    while(pointer1!=None and pointer2!= None):
        if pointer1.value > pointer2.value:
            tmp.next = pointer2
            tmp = tmp.next
            pointer2 = pointer2.next
        else:
            tmp.next = pointer1
            tmp = tmp.next
            pointer1 = pointer1.next
    while(pointer1!=None or pointer2!= None):
        if pointer1 == None:
            tmp.next = pointer2
            tmp = tmp.next
            pointer2 = pointer2.next
        else:
            tmp.next = pointer1
            tmp = tmp.next
            pointer1 = pointer1.next
            
        
    if b ==1 :
        return l2
    else:
        return l1
