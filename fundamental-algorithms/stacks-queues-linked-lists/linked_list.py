__author__ = 'cloudera'


class Node:
    def __init__(self, data, next_p=None, previous_p=None):
        self.data = data
        self.next = next_p
        self.previous = previous_p


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, n):
        if self.head is None:
            self.head = n
        else:
            self.head.previous_p = n
            n.next_p = self.head
            self.head = n

    def delete_node(self, n):
        if n.previous_p is None:
            self.head = n.next_p
        else:
            n.previous_p.next_p = n.next_p
        if n.next_p is not None:
            n.next_p.previous_p = n.previous_p

    def search_node(self, data):
        n = self.head
        while n is not None and n.data != data:
            n = n.next_p
        return n


def main():
    a = Node(1)
    l = LinkedList()
    l.insert_node(a)
    l.insert_node(Node(2))
    l.insert_node(Node(3))
    l.insert_node(Node(4))
    n = l.search_node(10)
    print n.data

if __name__ == '__main__':
    main()

