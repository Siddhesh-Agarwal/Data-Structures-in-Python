class StackOverflowError(Exception):
    """Exception raised when stack overflow occurs."""
    pass


class StackUnderflowError(Exception):
    """Exception raised when stack underflow occurs."""
    pass


class MaxStack:
    def __init__(self, limit):
        self.stack = []
        self.limit = limit
        self.length = 0

    def __str__(self):
        return '\n'.join(self.stack)

    def __len__(self):
        return self.length

    def __iter__(self):
        return iter(self.stack)

    def __getitem__(self, key):
        return self.stack[key]

    def push(self, value):
        if self.length < self.limit:
            self.length += 1
            self.stack.append(value)
        else:
            raise StackOverflowError("Stack overflow detected.")

    def pop(self):
        if self.length > 0:
            self.length -= 1
            return self.stack.pop()
        else:
            raise StackUnderflowError("Stack underflow detected.")

    def peek(self):
        return self.stack[-1]

    def clear(self):
        self.length = 0
        self.stack = []
