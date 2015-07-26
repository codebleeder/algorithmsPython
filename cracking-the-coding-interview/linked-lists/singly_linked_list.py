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


class Linked_list:
    def __init__(self, item):
        new_node = Node(item)
        self.head = new_node

    def append(self, item):
        previous_node = self.head
        current_node = previous_node.get_next()
        while current_node.get_next() is not None:
            current_node = current_node.get_next()
        previous_node.set_next(Node(item))

    def get_head(self):
        return self.head


#####################



