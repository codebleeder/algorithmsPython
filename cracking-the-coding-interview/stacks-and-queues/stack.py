__author__ = 'cloudera'
from node import Node


class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        new_node.set_next(self.top)
        self.top = new_node

    def pop(self):
        if self.top is not None:
            item = self.top.get_data()
            self.top = self.top.get_next()
            return item
        else:
            return None


# stack test
s = Stack()
s.push(3)
s.push(8)
print s.pop()

