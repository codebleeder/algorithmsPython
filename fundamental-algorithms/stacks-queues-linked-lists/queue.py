__author__ = 'cloudera'


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.q = [None]

    def enqueue(self, item):
        if self.tail is None:
            self.q[0] = item
            self.tail = 1
            self.head = 0
        else:
            self.q.append(item)
            self.tail += 1

    def dequeue(self):
        if self.head is not None and self.head < self.tail:
            val = self.q[self.head]
            self.head += 1
            return val
        else:
            print 'underflow'


def main():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print q.dequeue()
    print q.dequeue()
    print q.dequeue()

if __name__ == '__main__':
    main()
