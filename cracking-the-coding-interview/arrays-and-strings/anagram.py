__author__ = 'cloudera'


# sorting approach
def anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        return sorted(s1) == sorted(s2)


def anagram2(s1, s2):
    m1 = {}
    m2 = {}
    if len(s1) != len(s2):
        return False
    else:
        for i, j in zip(s1, s2):
            m1[i] = s1.count(i)
            m2[j] = s2.count(j)

        for i, j in zip(m1, m2):
            if i in m2 and m1[i] == m2[i] and j in m1 and m1[j] == m2[j]:
                pass
            else:
                return False
        return True

# main
print anagram2('dog', 'god')
print anagram2('dog', 'hod')

