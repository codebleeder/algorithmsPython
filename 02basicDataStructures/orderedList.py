__author__ = 'cloudera'
from node import Node


class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def size(self):
        currentNode = self.head
        size = 0
        while currentNode != None:
            currentNode = currentNode.getNext()
            size = size + 1
        return size

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

    def add(self, item):
        current_node = self.head
        previous_node = None
        stop = False
        while current_node is not None:
            if current_node.getData() > item:
                stop = True
            else:
                previous_node = current_node
                current_node = current_node.getNext()
        new_node = Node(item)
        if previous_node is None:
            self.head = new_node
            new_node.setNext(current_node)
        else:
            previous_node.setNext(new_node)
            new_node.setNext(current_node)

    def search(self, item):
        found = False
        current_node = self.head
        stop = False
        while found is False and stop is False and current_node is not None:
            if current_node.getData() == item:
                found = True
            elif current_node.getData() > item:
                stop = True
            else:
                current_node = current_node.getNext()
        return found



