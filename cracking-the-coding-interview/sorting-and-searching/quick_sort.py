__author__ = 'cloudera'


def quick_sort(a, first, last):
    if first < last:
        split_point = partition(a, first, last)
        quick_sort(a, first, split_point-1)
        quick_sort(a, split_point+1, last)


def partition(a, first, last):
    pivot = a[first]
    left_index = first + 1
    right_index = last
    done = False
    while not done:
        while a[left_index] <= pivot and left_index <= right_index:
            left_index += 1
        while a[right_index] >= pivot and left_index <= right_index:
            right_index -= 1
        if left_index < right_index:
            temp = a[left_index]
            a[left_index] = a[right_index]
            a[right_index] = temp
        else:
            done = True
    tmp = a[first]
    a[first] = a[right_index]
    a[right_index] = tmp
    print left_index
    return right_index

# test
a = [4, 5, 1, 9, 6]
quick_sort(a, 0, 4)
print a