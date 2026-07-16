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

    # FIFO
    def get_from_queue(self, target):
        temp_queue = Queue()

        found = None

        while not self.is_empty():
            item = self.pop()
            temp_queue.push(item)

            if item == target:
                found = item

        while not temp_queue.is_empty():
            self.push(temp_queue.pop())

        if found is None:
            raise ValueError(f'Елемент {target} не знайдено!')
        else:
            return found


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    queue = Queue()
    for i in lst:
        queue.push(i)

    print(queue.get_from_queue(6))
    print(queue.items)
