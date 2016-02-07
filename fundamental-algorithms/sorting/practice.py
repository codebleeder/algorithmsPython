__author__ = 'cloudera'


def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j-1
        while key < arr[i] and i >= 0:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key

a = [2, 8, 7, 1, 3, 5, 6, 4]
insertion_sort(a)
print a
