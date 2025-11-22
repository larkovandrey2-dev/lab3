class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class MinNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.min_head = None
        self.min_tail = None
        self._size = 0
    def dequeue(self):
        if self.head is None:
            raise ValueError("Queue is empty")
        value = self.head.data
        self.head = self.head.next
        self._size -= 1
        if self.head is None:
            self.tail = None
        if self.min_head and self.min_head.data == value:
            self.min_head = self.min_head.next
            if self.min_head is None:
                self.min_tail = None
        return value
    def enqueue(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._size += 1

        while self.min_tail and self.min_tail.data > value:
            self.min_tail = self.min_tail.prev
            if self.min_tail:
                self.min_tail.next = None
            else:
                self.min_head = None
        min_node = MinNode(value)
        if self.min_tail:
            min_node.prev = self.min_tail
            self.min_tail.next = min_node
            self.min_tail = min_node
        else:
            self.min_head = self.min_tail = min_node

    def front(self):
        if self.head is None:
            raise ValueError("Queue is empty")
        return self.head.data
    def is_empty(self):
        return self._size == 0
    def min(self):
        if self.min_head is None:
            raise ValueError("Queue is empty")
        return self.min_head.data
    def __len__(self):
        return self._size
