__author__ = 'cloudera'

from stack import Stack

def paranthesisChecker1(symbolString):
    index = 0
    balanced = True
    s = Stack()
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index = index + 1

    return balanced and s.isEmpty()

# test main
print paranthesisChecker1('()()(())')
print paranthesisChecker1('((()')