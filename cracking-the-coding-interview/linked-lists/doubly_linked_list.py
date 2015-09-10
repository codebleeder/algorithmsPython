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
class Doubly_linked_list:
    def __init__(self, item):
        self.head = Node(item)

    def add(self, num):
        new_node = Node(num)
        new_node.set_next(self.head)
        self.head.set_previous(new_node)
        self.head = new_node

    def delete(self, item):
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.get_data() != item:
                previous_node = current_node
                current_node = current_node.get_next()
            else:
                if previous_node is None:
                    self.head = current_node.get_next()
                elif current_node.get_next() is None:
                    previous_node.set_next(None)
                else:
                    previous_node.set_next(current_node.get_next())
                    current_node.get_next().set_previous(previous_node)
                return True
        return False

    def print_linked_list(self):
        current_node = self.head
        while current_node is not None:
            print current_node.get_data()
            current_node = current_node.get_next()