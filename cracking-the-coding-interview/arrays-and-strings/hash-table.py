__author__ = 'cloudera'


def unique(s):
    charset = {}
    for i in range(97, 123):
        charset[unichr(i)] = False

    for i in s:
        print i
        if charset[i] == False:
            charset[i] = True
        else:
            return False
    return True

# main
print unique('sharad')
print unique('shard')