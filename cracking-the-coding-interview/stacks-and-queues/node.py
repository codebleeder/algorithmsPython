__author__ = 'cloudera'


class Node:
    def __init__(self, item):
        self.next = None
        self.data = item

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node

    def get_data(self):
        return self.data


