"""Реалізуйте стек за допомогою однозв’язаного списку."""

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

class Stack:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return  self._head is None

    def push(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def pop(self):
        if self.is_empty():
            raise ValueError('Stack is empty')

        item = self._head.get_data()
        self._head = self._head.get_next()

        return item

    def peek(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self._head.get_data()


    def size(self):
        current = self._head
        count = 0
        while current is not None:
            current = current.get_next()
            count += 1

        return count

    def __repr__(self):
        representation = "<Stack: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

if __name__ == "__main__":
    stack = Stack()

    stack.push(10)
    stack.push(12)
    stack.push(13)

    print(stack)

    stack.pop()
    # stack.pop()
    # stack.pop()
    print(stack)

    print(stack.peek())

    print(stack.size())

