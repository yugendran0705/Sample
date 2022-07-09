# merge 2 lists sorted

def merge(l1, l2):
    l3 = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            l3.append(l1[i])
            i += 1
        else:
            l3.append(l2[j])
            j += 1
    if i == len(l1):
        l3.extend(l2[j:])
    else:
        l3.extend(l1[i:])
    return l3
l1=[1,2,3,4,5]
l2=[6,7,8,9,11]
l3=merge(l1,l2)
print(l3)

