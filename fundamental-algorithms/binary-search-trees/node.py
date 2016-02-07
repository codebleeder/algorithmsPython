class Node:
    """Node object for binary search tree"""
    def __init__(self, key, left = None, right = None, parent = None, data = None):
        self.parent = parent
        self.key = key
        self.data = data
        self.left = left 
        self.right = right 

    def get_key():
        return self.key 

    def get_parent():
        return self.parent

    def get_left():
        return self.left

    def get_right():
        return self.right 

    def set_left(left):
        self.left = left 

    def set_right(right):
        self.right = right 

    def set_data(data):
        self.data = data 
         