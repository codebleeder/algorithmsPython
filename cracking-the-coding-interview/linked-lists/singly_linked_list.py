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


class Singly_linked_list:
    def __init__(self, item):
        new_node = Node(item)
        self.head = new_node

    def add(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node

    def get_head(self):
        return self.head

    def print_linked_list(self):
        node = self.head
        while node is not None:
            print node.get_data()
            node = node.get_next()

    def delete(self, item):
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.get_data() != item:
                previous_node = current_node
                current_node = current_node.get_next()
            else:
                previous_node.set_next(current_node.get_next())
                return True
        return False

#####################



