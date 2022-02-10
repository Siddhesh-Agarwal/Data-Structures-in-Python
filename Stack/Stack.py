class Stack:
    def __init__(self):
        self.stack = []
        self.length = 0

    def __str__(self):
        return '\n'.join(self.stack)

    def __len__(self):
        return self.length

    def __iter__(self):
        return iter(self.stack)

    def __getitem__(self, key):
        return self.stack[key]

    def pop(self):
        self.length -= 1
        return self.stack.pop()

    def push(self, value):
        self.length += 1
        self.stack.append(value)

    def peek(self):
        return self.stack[-1]

    def clear(self):
        self.length = 0
        self.stack = []
