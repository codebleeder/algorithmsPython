__author__ = 'cloudera'


def rotate(m):
    layer_count = len(m)/2
    for layer in range(layer_count+1):
        start = layer
        end = len(m) - start
        print end
        for i in range(start, end):
            offset = i - start
            top_temp = m[start][i]
            m[start][i] = m[i][end-1]  # top -> right
            m[i][end-1] = m[end-1][end-1-i] # right -> bottom
            m[end-1][end-1-i] = m[end-1-i][start] # bottom -> left
            m[end-1-i][start] = top_temp


m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
rotate(m)
print m
