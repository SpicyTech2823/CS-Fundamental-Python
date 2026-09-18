class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)

stack = Stack()
# Pushing elements onto the stack
stack.push(1)
stack.push(2)   
stack.push(3)
stack.push(4)
print("Top:", stack.peek())

print("Pop:", stack.pop())
print("Pop:", stack.pop())

print("Size:", stack.size())   