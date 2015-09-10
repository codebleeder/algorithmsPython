__author__ = 'cloudera'


def remove_space(s):
    for i in range(len(s)-1, 0, -1):
        print i
        if s[i] == ' ':
            pass
        else:
            return s[0:i+1]


print remove_space('santa dasu  ')