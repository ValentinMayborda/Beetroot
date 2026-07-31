class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise ValueError("Pop from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        raise ValueError("Peek from empty queue")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
print(queue.pop())
print(queue.peek())
print(queue.size())
print(queue.is_empty())