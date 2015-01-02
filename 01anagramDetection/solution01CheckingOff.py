__author__ = 'sharad'

def anagramSolution1(s1, s2):
    list1 = list(s1)
    list2 = list(s2)

    pos1 = 1
    pos2 = 0
    matchFound = False
    matchFound2 = True

    # check if first alphabet is in second string
    # and print the position
    # if not say it isn't there
    for pos1 in range(len(list1)):
        #matchFound = False
        for pos2 in range(len(list2)):
            if list1[pos1] == list2[pos2]:
                matchFound = True
                #print 'found in position = ', pos2
            else:
                matchFound = matchFound or False

        print matchFound
        if matchFound == False:
            #print 'not found'
        matchFound2 = matchFound2 and matchFound

        matchFound = False
    #print 'matchfound2 = ', matchFound2
    return matchFound2

#main function:
anagramSolution1('earth', 'heart')
