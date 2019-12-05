# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    if l == None:
        return True
    extracted = []
    tmp = l
    while(tmp.next!=None):
        extracted.append(tmp.value)
        tmp = tmp.next
    extracted.append(tmp.value)
    n = len(extracted)
    a = True
    for i in range(0,n//2):
        if extracted[i] != extracted[n-i-1]:
            a = False
            break
    return a
