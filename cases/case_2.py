from collections import deque


class CircularBufferList:
    """
    Реализация класса посредством списка
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.size = 0
        self.head = 0
        self.tail = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, value):
        if self.is_full():
            self.head = (self.head + 1) % self.capacity
        else:
            self.size += 1
        self.buffer[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Buffer is empty")
        value = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return value

    def __str__(self):
        return str(self.buffer)


class CircularBufferDeque:
    """
    Реализация класса посредством использования collections.deque
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = deque(maxlen=capacity)

    def is_empty(self):
        return len(self.buffer) == 0

    def is_full(self):
        return len(self.buffer) == self.capacity

    def enqueue(self, value):
        self.buffer.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Buffer is empty")
        return self.buffer.popleft()

    def __str__(self):
        return str(list(self.buffer))