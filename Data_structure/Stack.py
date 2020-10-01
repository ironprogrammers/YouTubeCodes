# from collections import deque
# myStack = deque()

# myStack.append('a')
# myStack.append('b')
# myStack.append('c')

# print(myStack)

# myStack.pop()
# myStack.pop()
# myStack.pop()

# print(myStack)

# # myStack.pop()

# from queue import LifoQueue

# For threaded programs

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)