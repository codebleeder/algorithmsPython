__author__ = 'cloudera'

from queue import Queue

q = Queue()
print q.isEmpty()
q.enqueue(2)
print q.isEmpty()
q.enqueue(3)
print q.size()
q.dequeue()
print q.size()