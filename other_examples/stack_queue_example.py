class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []

    def peek(self):
        while self.first != []:
            self.second.append(self.first.pop())
        value = self.second.pop()
        self.first.append(value)
        while self.second != []:
            self.first.append(self.second.pop())
        print value

    def pop(self):
        while self.first != []:
            self.second.append(self.first.pop())
        value = self.second.pop()
        while self.second != []:
            self.first.append(self.second.pop())

    def put(self, value):
        self.first.append(value)

if __name__ == '__main__':
    queue = MyQueue()
    queue.put(42)
    queue.pop()
    queue.put(14)
    queue.peek()
    queue.put(28)
    queue.peek()
    queue.put(60)
    queue.put(78)
    queue.pop()
    queue.pop()