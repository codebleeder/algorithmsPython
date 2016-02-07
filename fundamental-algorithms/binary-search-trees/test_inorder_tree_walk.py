from node import Node 
from inorder_tree_walk import inorder_tree_walk

x = Node(6, Node(5), Node(7))
x.get_left().set_left(Node(2))
x.get_right().set_right(Node(5))

inorder_tree_walk(x)

