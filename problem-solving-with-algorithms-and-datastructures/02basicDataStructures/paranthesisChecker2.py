__author__ = 'cloudera'

from stack import Stack

def matches(open, close):
    openers = '([{'
    closers = ')]}'
    return openers.index(open) == closers.index(close)


def paranthesisChecker2(symbolString):
    index = 0
    balanced = True
    s = Stack()
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                print top
                if not matches(str(top), symbol):
                    balanced = False
        index = index + 1

    return balanced and s.isEmpty()



# test main
#print paranthesisChecker2('{{([][])}()}')
print paranthesisChecker2('[()()}')