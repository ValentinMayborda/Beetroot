"""Реалізуйте чергу за допомогою однозв’язаного списку."""


class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self, data):
        self._data = data

    def set_next(self, new_next):
        self._next = new_next


class Queue:
    def __init__(self):
        self._front = None
        self._rear = None

    def is_empty(self):
        return self._front is None

    def enqueue(self, item):
        temp = Node(item)

        if self._front is None:
            self._front = temp
            self._rear = temp
            return

        self._rear.set_next(temp)
        self._rear = temp

    def dequeue(self):

        if self._front is None:
            raise ValueError('Queue is empty')

        item = self._front.get_data()

        self._front = self._front.get_next()
        if self._front is None:
            self._rear = None

        return item

    def peek(self):
        if self.is_empty():
            raise ValueError('Queue is empty')

        return self._front.get_data()

    def size(self):
        current = self._front
        count = 0

        while current is not None:
            current = current.get_next()
            count += 1

        return count

    def __repr__(self):
        representation = "<Queue: "
        current = self._front
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"


if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(44)
    print(q)

    q.dequeue()
    print(q)

    print(q.peek())
    print(q.size())
