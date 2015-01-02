__author__ = 'cloudera'

def anagramSolution3(s1, s2):
    list1 = list(s1)
    list2 = list(s2)

    count1 = [0] * 26
    count2 = [0] * 26
    match = True

    for i in list1:
        count1[ord(i)-97] = count1[ord(i)-97] + 1

    for j in list2:
        count2[ord(j)-97] = count2[ord(j)-97] + 1
    #print count1
    #print count2
    for k in range(len(count1)):
        if count1[k] != count2[k]:
            match = False
            #print 'false'
    return match

# main
print anagramSolution3('earth', 'heart')