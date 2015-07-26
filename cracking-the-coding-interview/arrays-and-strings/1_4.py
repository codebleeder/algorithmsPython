__author__ = 'cloudera'


# O(n)
def replace_space(s):
    """1. calculate number of spaces in the first pass
    2. calculate the new length of the string
    3. replace each space with %20 in second pass"""
    s = list(s)
    space_count = 0
    old_index = len(s)-1
    for char in s:
        if char == ' ':
            space_count += 1

    #print space_count

    pad = [' ']*(space_count*2)
    s += pad
    new_index = len(s)-1

    while old_index >= 0:
        if s[old_index] == ' ':
            s[new_index] = '0'
            s[new_index-1] = '2'
            s[new_index-2] = '%'
            new_index -= 3
        else:
            s[new_index] = s[old_index]
            new_index -= 1
        old_index -= 1
    return ''.join(s)


def replace_space2(s):
    return s.replace(' ', '%20')

# test
print replace_space2('hi my name is')
print replace_space2('hi i am nicole    ')
print replace_space2('     hello')