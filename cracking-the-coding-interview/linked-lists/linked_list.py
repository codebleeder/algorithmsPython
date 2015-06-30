__author__ = 'cloudera'


class Node:
    def __init__(self, num):
        self.data = num
        self.next = None
        self.previous = None

    def set_data(self, num):
        self.data = num

    def get_data(self):
        return self.data

    def set_next(self, next_node):
        self.next = next_node

    def get_next(self):
        return self.next

    def set_previous(self, previous_node):
        self.previous = previous_node

    def get_previous(self):
        return self.previous

# linked list values
class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, num):
        new_node = Node(num)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.set_next(new_node)
            new_node.set_previous(self.head)
            new_node.set_next