class CrazyQueue:
    def __init__(self):
        self.first = []
        self.last = []

    def enqueue(self, value):
        length = len(self.first)
        for i in range(length):
            self.last.append(self.first.pop())
        self.last.append(value)
        return self

    def dequeue(self):
        length = len(self.last)
        for i in range(length):
            self.first.append(self.last.pop())
        self.first.pop()
        return self

    def peek(self):
        if self.first:
            return self.first[-1]
        return self.last[0] if self.last else None

# Test
myQueue = CrazyQueue()
print(myQueue.peek())
myQueue.enqueue('Joy')
myQueue.enqueue('Matt')
myQueue.enqueue('Pavel')
print(myQueue.peek())
print("========")
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())
print("========")
print(myQueue.peek())
print(myQueue)
