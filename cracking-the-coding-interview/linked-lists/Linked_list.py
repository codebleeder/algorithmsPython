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

# addition of 2 numbers
def add(l1, l2):
    n1 = l1.get_head()
    n2 = l2.get_head()
    l3 = Linked_list(0)
    carry = 0
    while n1.get_next() is not None:
        sum = n1.get_data() + n2.get_data()
        l3.append(sum % 10)
        if sum > 9:
            carry = 1
        else:
            carry = 0

    return l3

l1 = Linked_list(1)
l2 = Linked_list(2)
add(l1, l2)

class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        new_node.set_next(self.top)
        self.top = new_node

    def pop(self):
        if (self.top is not None):
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

#####################


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

