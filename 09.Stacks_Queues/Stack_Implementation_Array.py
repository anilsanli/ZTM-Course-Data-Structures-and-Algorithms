class Stack:
    def __init__(self):
        self.array = []

    def peek(self):
        if self.array:
            return self.array[-1]
        else:
            return None

    def push(self, value):
        self.array.append(value)
        return self

    def pop(self):
        if self.array:
            self.array.pop()
        return self

# Test
myStack = Stack()
myStack.peek()
myStack.push('google')
myStack.push('ztm')
myStack.push('discord')
myStack.peek()
myStack.pop()
myStack.pop()
myStack.pop()
