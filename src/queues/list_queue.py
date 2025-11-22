class ListQueue:
    def __init__(self):
        self.queue = []
        self.mins = []
    def enqueue(self, value):
        self.queue.append(value)
        while self.mins and self.mins[-1] > value:
            self.mins.pop()
        self.mins.append(value)
    def dequeue(self):
        if len(self.queue) == 0:
            raise ValueError("Queue is empty")
        value = self.queue.pop(0)
        if self.mins[0] == value:
            self.mins.pop(0)
        return value
    def front(self):
        if len(self.queue) == 0:
            raise ValueError("Queue is empty")
        return self.queue[0]
    def is_empty(self):
        return len(self.queue) == 0
    def min(self):
        return self.mins[0]
    def __len__(self):
        return len(self.queue)
