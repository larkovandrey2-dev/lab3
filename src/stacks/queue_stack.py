from collections import deque

class QueueStack:
    def __init__(self):
        self.queue = deque()
        self.mins = deque()
        self.size = 0
    def push(self, value):
        self.queue.append(value)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
            self.mins.appendleft(self.mins.pop())
        self.size += 1
    def pop(self):
        if not self.queue:
            raise ValueError("Stack is empty")
        self.size -= 1
        return self.queue.popleft()
    def peek(self):
        if not self.queue:
            raise ValueError("Stack is empty")
        return self.queue[0]
    def is_empty(self):
        return self.size == 0
    def min(self):
        if not self.mins:
            raise ValueError("Stack is empty")
        return self.mins[0]
    def __len__(self):
        return self.size

class QueueStackList:
    def __init__(self):
        self.queue = []
        self.mins = []
        self.size = 0
    def push(self, value):
        new_min = value if not self.mins else min(self.mins[0], value)
        self.queue = [value] + self.queue
        self.mins = [new_min] + self.mins
        self.size += 1
    def pop(self):
        if not self.queue:
            raise ValueError("Stack is empty")
        return self.queue.pop(0)
    def peek(self):
        if not self.queue:
            raise ValueError("Stack is empty")
        return self.queue[0]
    def is_empty(self):
        return self.size == 0
    def min(self):
        if not self.mins:
            raise ValueError("Stack is empty")
        return self.mins[0]
    def __len__(self):
        return self.size
