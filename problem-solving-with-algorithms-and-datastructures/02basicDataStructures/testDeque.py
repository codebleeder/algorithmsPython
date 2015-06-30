__author__ = 'cloudera'
from deque import Deque

d = Deque()

# check isEmpty() and addFront()
print d.isEmpty()  # True
d.addFront(3)
print d.isEmpty()  # False
d.removeFront()
print d.isEmpty()  # True

# check size() and addRear()
print d.size()  # 0
d.addRear(4)
print d.size()  # 1
d.removeRear()
print d.size()  # 0



