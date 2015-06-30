__author__ = 'cloudera'


class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

    def setData(self, item):
        self.data = item

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

