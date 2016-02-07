__author__ = 'cloudera'


class Stack:
    def __init__(self):
        self.top = None
        self.s = []

    def push(self, item):
        self.s.append(item)
        if self.top is None:
            self.top = 0
        else:
            self.top += 1

    def is_empty(self):
        return self.top is None

    def pop(self):
        if self.is_empty() is False:
            val = self.s[self.top]
            if self.top == 0:
                self.top = None
            else:
                self.top -= 1
            return val


def main():
    s = Stack()
    print s.pop()
    s.push(7)
    s.push(8)
    print s.pop()
    print s.pop()
    print s.pop()

if __name__ == '__main__':
    main()