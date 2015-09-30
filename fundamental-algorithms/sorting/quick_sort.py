__author__ = 'cloudera'


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def partition(arr, p, r):
    key = arr[r]
    i = p-1
    j = p
    while j < r:
        if arr[j] <= key:
            i += 1
            swap(arr, i, j)

        j += 1
    swap(arr, i+1, r)
    return i+1


def quick_sort(arr, p, r):
    if r > p:
        q = partition(arr, p, r)
        quick_sort(arr, p, q-1)
        quick_sort(arr, q+1, r)

a = [2, 8, 7, 1, 3, 5, 6, 4]
#print partition(a, 0, len(a)-1)

quick_sort(a, 0, len(a)-1)
print a
# output: 2,1,3,4,7,5,6,8