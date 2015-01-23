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


class UnorderedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        if self.head.getNext() is None:
            self.tail = self.head

    def size(self):
        currentNode = self.head
        size = 0
        while currentNode != None:
            currentNode = currentNode.getNext()
            size = size + 1
        return size

    def search(self, item):
        currentNode = self.head
        found = False
        while found == False and currentNode != None:
            if currentNode.getData() == item:
                found = True
            else:
                currentNode = currentNode.getNext()  # move on to the next node
        return found

    def remove(self, item):  # assuming item is present
        currentNode = self.head
        previousNode = None
        found = False
        while found is False and currentNode is not None:
            if currentNode.getData() == item:
                found = True
            else:
                previousNode = currentNode
                currentNode = currentNode.getNext()  # move on to the next node
        # item has been found and is in currentNode
        if previousNode is None:
            self.head = currentNode.getNext()
        else:
            previousNode.setNext(currentNode.getNext())

    def append(self, item):
        # node = self.head
        # traversing the linked list
        # while node.getNext() is not None:
        #     node = node.getNext()
        # new_node = Node(item)
        # node.setNext(new_node)
        new_node = Node(item)
        # point the old tail to new_node
        self.tail.setNext(new_node)
        # make the new_node the new tail
        self.tail = new_node

    # assumption: the item is not already in the list
    # there are enough existing items to have position pos
    def insert(self, pos, item):
        current_pos = 0
        current_node = self.head
        previous_node = None
        while current_pos != pos:
            previous_node = current_node
            current_node = current_node.getNext()
            current_pos = current_pos + 1
        # reached the desired position
        new_node = Node(item)
        previous_node.setNext(new_node)
        new_node.setNext(current_node)

    # assumption: item is in the list
    def index(self, item):
        current_node = self.head
        current_pos = 0
        while current_node.getData() != item:
            current_pos = current_pos + 1
            current_node = current_node.getNext()
        return current_pos

    # def pop(self):
    #     # traverse at the end of the list
    #     # get the data
    #     # remove the last node
    #     current_node = self.head
    #     previous_node = None
    #     while current_node.getNext() is not None:
    #         previous_node = current_node
    #         current_node = current_node.getNext()
    #     data = current_node.getData()
    #     previous_node.setNext(current_node.getNext())
    #     return data

    def pop(self, pos=None):
        # traverse to the specified position
        # get the data
        # delete the node and return data
        if pos is None:
            current_node = self.head
            previous_node = None
            while current_node.getNext() is not None:
                previous_node = current_node
                current_node = current_node.getNext()
            data = current_node.getData()
            previous_node.setNext(current_node.getNext())
            return data
        else:
            current_node = self.head
            previous_node = None
            current_pos = 0
            while current_pos != pos:
                previous_node = current_node
                current_node = current_node.getNext()
                current_pos = current_pos + 1
            data = current_node.getData()
            previous_node.setNext(current_node.getNext())
            return data
