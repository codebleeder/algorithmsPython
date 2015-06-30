__author__ = 'cloudera'
from deque import Deque

def palindromeChecker(inputString):
    d = Deque()
    for char in inputString:
        d.addRear(char)

    isPalindrome = True
    while d.size() > 1:
        front = d.removeFront()
        rear = d.removeRear()
        if front != rear:
            isPalindrome = False

    return isPalindrome

# main
print palindromeChecker('sharad')
print palindromeChecker('madam')