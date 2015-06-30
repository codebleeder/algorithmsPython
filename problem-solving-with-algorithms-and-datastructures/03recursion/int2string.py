__author__ = 'cloudera'


def int2string(num, base):
    conv_string = '0123456789ABCDEF'
    if num < base:
        return conv_string[num]
    else:
        return int2string(num//base, base) + int2string(num % base, base)


def reverse(s):
    if len(s) == 1:
        return s[0]
    else:
        return reverse(s[1:]) + reverse(s[0])


def remove_whitespace(s):
    if len(s) == 1:
        if s[0] == ' ':
            return ''
        else:
            return s[0]
    else:
        return remove_whitespace(s[0]) + remove_whitespace(s[1:])


def is_palindrome(s):
    if len(s) == 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False

#print int2string(1453, 16)
#print reverse('kayak')
print is_palindrome(remove_whitespace('live not on evil'))