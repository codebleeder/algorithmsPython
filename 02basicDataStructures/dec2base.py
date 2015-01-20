# converts a decimal number to any base
__author__ = 'cloudera'
from stack import Stack


def base_converter(decNum, base):
    s = Stack()
    digits = "0123456789ABCDEF"
    while decNum > 0:
        remainder = decNum % base
        #print remainder
        s.push(remainder)
        #print s.peek()
        decNum = decNum // base
    output = ""

    while s.size() > 0:
        output = output + digits[s.pop()]
        #print s.pop()
    return output

# main - test
print base_converter(26, 2)