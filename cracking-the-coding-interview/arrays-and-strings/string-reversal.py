__author__ = 'cloudera'


def reverse(s):
    a = 0
    b = len(s)-1
    while a <= len(s)-1:
        print a, b
        tmp = s[a]
        print s[a], s[b], tmp
        #s[a] = s[b]
        #s[b] = tmp
        a += 1
        b -= 1
    return s[::-1]

print reverse('sharad')