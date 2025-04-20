class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.rear == self.front

    def enqueue(self, item):
        self.rear += 1
        self.items[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            raise IndexError('queue is empty')
        self.front += 1
        item = self.items[self.front]
        self.items[self.front] = None
        return item

queue = Queue(5)
queue.enqueue('A')
print(queue.items)
queue.dequeue()
print(queue.items)
print(queue.front, queue.rear)