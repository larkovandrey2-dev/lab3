class StacksQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        self._size = 0
    def enqueue(self, value):
        new_min = value if not self.in_stack else min(value, self.in_stack[-1][1])
        self.in_stack.append((value, new_min))
        self._size += 1
    def dequeue(self):
        if len(self.in_stack) == 0 and len(self.out_stack) == 0:
            raise ValueError("Queue is empty")
        if len(self.out_stack) == 0:
            while self.in_stack:
                val, _ = self.in_stack.pop()
                new_min = val if not self.out_stack else min(val, self.out_stack[-1][1])
                self.out_stack.append((val, new_min))
        self._size -= 1
        return self.out_stack.pop()[0]
    def front(self):
        if self._size == 0:
            raise ValueError("Queue is empty")
        return self.out_stack[-1][0] if self.out_stack else self.in_stack[0][0]
    def is_empty(self):
        return self._size == 0
    def min(self):
        if len(self.in_stack) == 0 and len(self.out_stack) == 0:
            raise ValueError("Queue is empty")
        elif len(self.out_stack) == 0:
            return self.in_stack[-1][1]
        elif len(self.in_stack) == 0:
            return self.out_stack[-1][1]
        else:
            return min(self.in_stack[-1][1], self.out_stack[-1][1])
    def __len__(self):
        return self._size
