def find_min_idx(a):
    n = len(a)
    min_idx=0

    for i in range(0,n):
        if a [min_idx]>a[i]:
            min_idx = i

    return min_idx

def sel_sort(a:list):
    result = []

    while a:
        min_idx=find_min_idx(a)
        value = a.pop(min_idx)
        result.append(value)

    return result

v = [2,4,5,1,3]
print(sel_sort(v))