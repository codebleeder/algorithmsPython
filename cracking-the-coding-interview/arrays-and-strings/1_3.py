__author__ = 'cloudera'


# O(n) complexity
def anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        letters = [0]*256
        # count frequency in s1
        for char in s1:
            letters[ord(char)] += 1

        # compare with char counts in s2
        for char in s2:
            if letters[ord(char)]-1 < 0:
                return False
        return True


def anagram2(s1, s2):
    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)


# test
print anagram2('sharad', 'darahs')
print anagram2('sharad', 'shard')

# declare an integer array with space for 256 characters
