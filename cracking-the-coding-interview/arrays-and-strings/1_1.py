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


def unique4(s):
    if len(s) > 128:
        return False
    char_set = [None] * 128
    for i in range(len(s)):
        val = s[i]
        if char_set[ord(val)]:
            return False
        char_set[ord(val)] = True
    return True

# main
print unique4('sharad')
print unique4('shard')
