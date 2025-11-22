class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.min_under = None
class LinkedStack:
    def __init__(self):
        self.top = None
        self._size = 0
    def push(self,item):
        node = Node(item)
        if self.top is None:
            node.min_under = node.data
        else:
            node.min_under = min(self.top.min_under, node.data)
        node.next = self.top
        self.top = node
        self._size += 1
    def pop(self):
        if self.top is None:
            raise ValueError("Stack is empty")
        value = self.top.data
        self.top = self.top.next
        self._size -= 1
        return value
    def peek(self):
        if self.top is None:
            raise ValueError("Stack is empty")
        return self.top.data
    def is_empty(self):
        return self._size == 0
    def min(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.top.min_under
    def __len__(self):
        return self._size
