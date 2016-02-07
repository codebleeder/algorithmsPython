__author__ = 'cloudera'


def max_subarray(arr):
    sum = 0
    max_num = 0
    start = end = 0
    for i in arr:
        if sum+i < 0:
            max_num = sum
            sum = 0
        else:
            sum = sum + i
            max_num = max(sum, max_num)
    return max_num


def max_subarray(arr):
    sum = 0
    max_num = 0
    start = end = 0
    for i in arr:
        if sum+i < 0:
            max_num = sum
            sum = 0
        else:
            sum = sum + i
            max_num = max(sum, max_num)
    return max_num

print max_subarray([10, -7, 8, -8, 6, -3, 6, -21, 5, -2, 1])



