__author__ = 'cloudera'


def merge_sort(a):
    if len(a) > 1:
        middle = len(a)/2
        left = a[:middle]
        right = a[middle:]
        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            a[k] = left[i]
            k += 1
            i += 1

        while j < len(right):
            a[k] = right[j]
            k += 1
            j += 1


a = [1, 5, 9, 2, 4]
merge_sort(a)
print a