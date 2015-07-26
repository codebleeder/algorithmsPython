__author__ = 'cloudera'
from singly_linked_list import Singly_linked_list


# addition of 2 numbers
def add(l1, l2):
    n1 = l1.get_head()
    n2 = l2.get_head()
    l3 = Singly_linked_list(0)
    first = True
    carry = 0
    while n1 is not None:
        sum = n1.get_data() + n2.get_data() + carry
        digit = sum % 10
        carry = sum/10
        print 'digit = ', digit
        print 'carry = ', carry
        l3.add(digit)
        if first:
            l3.delete(0)
        n1 = n1.get_next()
        n2 = n2.get_next()
    l3.add(carry)
    l3.print_linked_list()
    return l3

# test
ll1 = Singly_linked_list(5)
ll1.add(2)
ll1.add(3)
ll2 = Singly_linked_list(7)
ll2.add(9)
ll2.add(2)
add(ll1, ll2)
