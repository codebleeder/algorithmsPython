__author__ = 'cloudera'


def insertion_sort(a):
    a_len = len(a)
    for j in range(1, a_len):
        key = a[j]
        i = j-1
        while i >= 0 and a[i] > key:
            a[i+1] = a[i]
            i -= 1
        a[i+1] = key
    return a

print insertion_sort([1,7,3,6,2])