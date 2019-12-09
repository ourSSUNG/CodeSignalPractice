def containsDuplicates(a):
    dic = {}
    for i in range(0,len(a)):
        dic[a[i]] = 1
    if len(list(dic.keys()))== len(a):
        return False
    return True
