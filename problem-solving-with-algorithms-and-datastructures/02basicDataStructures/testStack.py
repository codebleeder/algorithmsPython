__author__ = 'cloudera'
from stack import Stack

a = Stack()
print a.isEmpty()
a.push(1)
a.push('sharad')
print a.peek()
print a.size()
a.pop()
print a.peek()
print a.size()