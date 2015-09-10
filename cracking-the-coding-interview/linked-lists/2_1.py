__author__ = 'cloudera'
from singly_linked_list import Singly_linked_list


# with hash-table
def duplicates(linked_list):
    unique = {}
    current_node = linked_list.get_head()
    previous_node = None
    while current_node is not None:
        if current_node.get_data() in unique:
            #print 'in unique'
            previous_node = current_node
            current_node = current_node.get_next()
            linked_list.delete(previous_node.get_data())
        else:
            unique[current_node.get_data()] = True
            previous_node = current_node
            current_node = current_node.get_next()
    #print unique
    linked_list.print_linked_list()
    return linked_list


def duplicates2(linked_list):
    current = linked_list.get_head()
    while current is not None:
        runner = current
        while runner.get_next() is not None:
            if runner.get_next().get_data() == runner.get_data():
                runner.set_next(runner.get_next().get_next())
            else:
                runner = runner.get_next()
        current = current.get_next()
    linked_list.print_linked_list()
    return linked_list

# test
l1 = Singly_linked_list(2)
l1.add(9)
l1.add(8)
l1.add(2)
l1.add(1)
l2 = duplicates2(l1)