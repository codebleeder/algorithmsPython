__author__ = 'cloudera'
from node import Node


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.tail == None:
            new_node.set_next = None
            self.head = new_node
        else:
            new_node.set_next = self.tail.get_next()
        self.tail = new_node

    def dequeue(self):
        item = self.head.get_data()
        prev_node = self.tail
        curr_node = prev_node.get_next()
        while curr_node is not None:
            curr_node = curr_node.get_next()
            prev_node = prev_node.get_next()
        self.head = prev_node
        return item

# test queue
q = Queue()
q.enqueue(1)
q.enqueue(8)
print q.dequeue()
