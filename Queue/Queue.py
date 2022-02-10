class Queue:
    def __init__(self):
        self.queue = []
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        s = str(self.queue)
        return s[1:-1]

    def __iter__(self):
        return iter(self.queue)

    def __getitem__(self, key):
        return self.queue[key]

    def add(self, key):
        self.length += 1
        self.queue.append(key)

    def pop(self):
        self.length -= 1
        temp, *self.queue = self.queue
        return temp

    def clear(self):
        self.length = 0
        self.queue = []
