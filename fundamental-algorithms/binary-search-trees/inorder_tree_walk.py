def inorder_tree_walk(node):
    if node != None:
        inorder_tree_walk(node.get_left())
        print node.get_key()
        inorder_tree_walk(node.get_right())
