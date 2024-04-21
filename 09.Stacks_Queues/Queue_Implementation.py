class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return self

    def dequeue(self):
        if not self.first:
            return None
        if self.first == self.last:
            self.last = None
        self.first = self.first.next
        self.length -= 1
        return self

# Test
myQueue = Queue()
myQueue.enqueue("Joy")
myQueue.enqueue("Matt")
myQueue.enqueue("Pavel")
myQueue.enqueue("Samir")
myQueue.dequeue()
myQueue.peek()
print(myQueue)
# Joy
# Matt
# Pavel
# Samir
