__author__ = 'cloudera'

from singly_linked_list import Singly_linked_list
from doubly_linked_list import Doubly_linked_list

if False:
    l1 = Singly_linked_list(1)
    l1.add(7)
    l1.print_linked_list()
    l1.delete(1)
    l1.print_linked_list()

l2 = Doubly_linked_list(3)
l2.add(2)
l2.print_linked_list()
print l2.delete(3)
l2.print_linked_list()





