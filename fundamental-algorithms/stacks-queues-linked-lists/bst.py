__author__ = 'cloudera'


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.parent = None
        self.data = data


class Bst:
    def __init__(self, data):
        self.root = Node(data)

    def inorder_tree_walk(self, n):
        if n is not None:
            self.inorder_tree_walk(n.left)
            print n.data
            self.inorder_tree_walk(n.right)

    def tree_search(self, node, data):
        while node is not None and data != node.data:
            if node.data < data:
                node = node.right
            else:
                node = node.left
        return node

    def tree_minimum(self, node):
        while node.left is not None:
            node = node.left
        return node

    def tree_maximum(self, node):
        while node.right is not None:
            node = node.right
        return node

    def tree_successor(self, node):
        if node.right is not None:
            return self.tree_minimum(node.right)
        y = node.parent
        # print y.data
        # while node == y.right and y is not None:
        #     node = y
        #     y = node.parent
        return y


    def tree_insert(self, node):
        x = self.root
        y = None
        while x is not None:
            y = x
            if x.data > node.data:
                x = x.left
            else:
                x = x.right
        if y is None:
            self.root = node
        elif node.data > y.data:
            y.right = node
        else:
            y.left = node
        node.parent = y


def main():
    bst = Bst(7)
    bst.tree_insert(Node(9))
    bst.tree_insert(Node(6))
    bst.tree_insert(Node(10))
    bst.tree_insert(Node(8))
    bst.inorder_tree_walk(bst.root)
    print 'tree minimum = ', bst.tree_minimum(bst.root).data
    print 'tree_search(8) = ', bst.tree_search(bst.root, 8).data
    print 'tree maximum = ', bst.tree_maximum(bst.root).data
    print 'successor of 7 = ', bst.tree_successor(bst.root).data


if __name__ == '__main__':
    main()