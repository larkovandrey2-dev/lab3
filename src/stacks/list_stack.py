class Stack:
    def __init__(self):
        self._size = 0
        self.stack = []
        self.mins = []
    def push(self, value):
        if not self.mins:
            self.mins.append(value)
        else:
            self.mins.append(min(value, self.mins[-1]))
        self.stack.append(value)
        self._size += 1
    def pop(self):
        if self._size == 0:
            raise ValueError("Stack is empty")
        self.mins.pop()
        self._size -= 1
        return self.stack.pop()
    def peek(self):
        if self._size == 0:
            raise ValueError("Stack is empty")
        return self.stack[-1]
    def is_empty(self):
        return self._size == 0
    def min(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.mins[-1]
    def __len__(self):
        return self._size
