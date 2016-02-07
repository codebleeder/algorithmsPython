__author__ = 'cloudera'


def diff(n, arr):
    j = 0 # left to right
    k = n-1 # right to left
    d1 = 0
    d2 = 0
    for i in xrange(n):
        d1 += arr[i][j]
        j += 1
        d2 += arr[i][k]
        k -= 1
    return abs(d1-d2)

print diff(3, [[11,2,4],[4,5,6],[10,8,-12]])