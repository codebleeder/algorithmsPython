__author__ = 'cloudera'
from queue import Queue

def hotPotato(nameList, count):
    q = Queue()

    for name in nameList:
        q.enqueue(name)

    while q.size() > 1:
        for i in range(count):
            out = q.dequeue()
            q.enqueue(out)
        q.dequeue()

    return q.dequeue()

# test
print hotPotato(['sharad', 'mario', 'sonic', 'naruto', 'luffy', 'zoro'], 7)
