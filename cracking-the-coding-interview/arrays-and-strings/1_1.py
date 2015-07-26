__author__ = 'cloudera'


def unique(s):
    charset = {}
    for i in range(97, 123):
        charset[unichr(i)] = False

    for i in s:
        #print i
        if charset[i] == False:
            charset[i] = True
        else:
            return False
    return True


def unique2(s):
    for letter in s:
        if s.count(letter) > 1:
            return False
    return True


def unique3(s):
    unique_map = {}
    for letter in s:
        if letter in unique_map:
            return False
        else:
            unique_map[letter] = True
    return True

# main
print unique3('sharad')
print unique3('shard')