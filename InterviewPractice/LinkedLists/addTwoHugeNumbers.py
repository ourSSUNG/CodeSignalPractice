# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def addTwoHugeNumbers(a, b):
    tmp1 = a
    tmp2 = b
    list1 = []
    list2 = []
    list3 = []
    while(tmp1!=None):
        list1.append(tmp1.value)
        tmp1 = tmp1.next
    while(tmp2!=None):
        list2.append(tmp2.value)
        tmp2 = tmp2.next
    len1 = len(list1)
    len2 = len(list2)
    i=0
    numtmp=0
    uppercase = 0
    while(len1-i>0 or len2-i>0):
        if len1-i > 0:
            numtmp = numtmp + list1[len1-i-1]
        if len2-i > 0:
            numtmp = numtmp + list2[len2-i-1]
        if uppercase == 1:
            numtmp = numtmp + 1
        if numtmp > 9999:
            uppercase = 1
            numtmp = numtmp - 10000
        else:
            uppercase = 0
        list3.append(numtmp)
        i = i+1
        numtmp = 0
    if ( uppercase == 1):
        list3.append(1)
    len3 = len(list3)
    nodelist = []
    for i in range(0,len3):
        nodelist.append(ListNode(list3[len3-i-1]))
    for i in range(0,len3-1):
        nodelist[i].next = nodelist[i+1]
    return nodelist[0]
        
