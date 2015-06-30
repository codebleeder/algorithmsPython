__author__ = 'cloudera'


class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print 'no items!'

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

#main program
s = Stack()
print s.is_empty()
s.push(1)
s.push(2)
s.push(3)
print s.is_empty()
print s.size()
print s.pop()
print s.pop()
print s.pop()
s.pop()