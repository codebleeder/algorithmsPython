__author__ = 'cloudera'


class Node:
    def __init__(self):
        self.parent = None
        self.right = None
        self.left = None
        self.key = None

    def get_parent(self):
        return self.parent

    def set_parent(self, node_in):
        self.parent = node_in

    def get_right(self):
        try:
            return self.right
        except ValueError:
            print 'leaf node'

    def set_right(self, node_in):
        self.right = node_in

    def get_left(self):
        if self.left is not None:
            return self.left
        else:
            print 'leaf node'

    def set_left(self, node_in):
        self.left = node_in

    def get_key(self):
        return self.key

    def set_key(self, key_in):
        self.key = key_in


def inorder_tree_walk(x):
    if x is not None:
        inorder_tree_walk(x.get_left())
        print x.get_key()
        inorder_tree_walk(x.get_right())


def preorder_tree_walk(x):
    if x is not None:
        print x.get_key()
        preorder_tree_walk(x.get_left())
        preorder_tree_walk(x.get_right())


def postorder_tree_walk(x):
    if x is not None:
        preorder_tree_walk(x.get_left())
        preorder_tree_walk(x.get_right())
        print x.get_key()


def insert_node(root, x):
    p = None
    q = root
    while q is not None:
        p = q
        if q.get_key() > x.get_key():
            q = q.get_left()
        else:
            q = q.get_right()
    if p.get_key() > x.get_key():
        p.set_left(x)
    else:
        p.set_right(x)

x = Node()
y = Node()
z = Node()

x.set_key(5)
y.set_key(3)
z.set_key(6)
x.set_left(y)
x.set_right(z)
y.set_parent(x)
z.set_parent(x)

a = Node()
a.set_key(8)

#insert_node(x, a)
#inorder_tree_walk(x)
#preorder_tree_walk(x)
#postorder_tree_walk(x)
