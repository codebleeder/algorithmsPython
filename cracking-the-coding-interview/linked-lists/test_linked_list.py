__author__ = 'cloudera'

from singly_linked_list import Singly_linked_list
from doubly_linked_list import Doubly_linked_list

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





