def generateMatrix(n):
    dir = 0
    top = left = 0
    right = n-1
    bottom = n-1
    mat = [None]*n
    for i in xrange(n):
        mat[i] = [None]*n
    element = 1
    while top <= bottom and left <= right:
        if dir==0:
            for i in xrange(left, right+1):
                mat[top][i] = element
                element += 1
            print dir, mat
            top += 1
            dir = 1
        elif dir == 1:
            for i in xrange(top,bottom+1):
                mat[i][right] = element
                element += 1
            print dir, mat
            right -= 1
            dir = 2
        elif dir==2:
            for i in xrange(right,left-1,-1):
                mat[bottom][i] = element
                element += 1
            print dir, mat
            bottom -= 1
            dir = 3
        else:
            for i in xrange(bottom, top-1, -1):
                mat[i][left] = element
                element += 1
            print dir, mat
            left += 1
            dir = 0
    return mat

print generateMatrix(3)