__author__ = 'cloudera'


def merge(a1, a2):
    len_a1 = len(a1)
    len_a2 = len(a2)
    i = 0
    j = 0
    k = 0
    a = [None] * (len(a1)+len(a2))
    while i < len_a1 and j < len_a2:
        if a1[i] < a2[j]:
            a[k] = a1[i]
            i += 1
            k += 1
        else:
            a[k] = a2[j]
            j += 1
            k += 1

    while i < len_a1:
        a[k] = a1[i]
        k += 1
        i += 1
    while j < len_a2:
        a[k] = a2[j]
        k += 1
        j += 1
    return a


def merge_sort(a):
    if len(a) > 1:
        p = 0
        q = len(a)
        r = len(a)/2
        left = merge_sort(a[p:r])
        right = merge_sort(a[r:q])
        return merge(left, right)
    return a

print merge_sort([8, 1, 12, 2, 14, 5])
