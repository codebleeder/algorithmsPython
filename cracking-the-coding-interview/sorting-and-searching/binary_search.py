__author__ = 'cloudera'


def binary_search(a, item):
    first = 0
    last = len(a)-1

    while first <= last:
        middle = (first+last)//2
        if a[middle] == item:
            return True
        elif a[middle] < item:
            first = middle+1
        else:
            last = middle-1
    return False

a = [1, 2, 3, 6, 9, 7]
print binary_search(a, 8)