__author__ = 'cloudera'

class Deque:

    def __init__(self):
        self.l = []

    def addFront(self, item):
        self.l.insert(0, item)

    def addRear(self, item):
        self.l.append(item)

    def removeFront(self):
        return self.l.pop(0)

    def removeRear(self):
        return self.l.pop()

    def isEmpty(self):
        return len(self.l) == 0

    def size(self):
        return len(self.l)

