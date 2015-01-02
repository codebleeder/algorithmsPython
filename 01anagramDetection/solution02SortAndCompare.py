__author__ = 'cloudera'

def anagramSolution2(s1, s2):
    list1 = list(s1)
    list2 = list(s2)
    list1.sort()  # complexity will depend on these sort steps
    list2.sort()
    match = True

    #compare w.r.t position
    pos = 0
    for pos in range(len(list1)):
        if list1[pos] != list2[pos]:
            match = False

    return match

#main
print anagramSolution2('earth', 'heart')

