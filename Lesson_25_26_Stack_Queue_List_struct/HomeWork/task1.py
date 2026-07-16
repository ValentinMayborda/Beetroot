"""Завдання 1. Розширити UnsortedList
Реалізуйте такі методи для класу UnsortedList:

+ append(item) — додає елемент у кінець списку.
index(item) — повертає індекс першого входження елемента.
pop() — видаляє та повертає останній елемент списку.
insert(pos, item) — вставляє елемент у вказану позицію.

Також реалізуйте метод:
slice(start, stop)
Цей метод повинен приймати два параметри:
start — початковий індекс;
stop — кінцевий індекс (не включається).
Метод має повернути копію списку, яка містить елементи від start до stop - 1."""

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


class UnsortedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def append(self, item):
        temp = Node(item)

        if self._head is None:
            self._head = temp
            return

        current = self._head
        while current.get_next() is not None:
            current = current.get_next()

        current.set_next(temp)

    def index(self, item):
        current = self._head
        index = 0

        while current is not None:
            if current.get_data() == item:
                return index

            current = current.get_next()
            index += 1

        raise ValueError('Item not found')

    def pop(self):

        if self.is_empty():
            raise ValueError('List is empty')

        current = self._head
        previous = None

        while current.get_next() is not None:
            previous = current
            current = current.get_next()
        item = current.get_data()

        if previous is None:
            self._head = None
        else:
            previous.set_next(None)

        return item

    def insert(self, pos, item):

        temp = Node(item)

        if pos == 0:
            temp.set_next(self._head)
            self._head = temp
            return

        current = self._head
        previous = None
        index = 0

        while index < pos:
            previous = current
            current = current.get_next()
            index += 1

        temp.set_next(current)
        previous.set_next(temp)

    def slice(self, start, stop):
        current = self._head
        index = 0

        while index < start:
            current = current.get_next()
            index += 1
        result = UnsortedList()

        while index < stop:
            result.append(current.get_data())

            current = current.get_next()
            index += 1

        return result

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def __repr__(self):
        representation = "<UnsortedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"


if __name__ == "__main__":
    my_list = UnsortedList()
    my_list.add(15)
    my_list.add(10)
    my_list.add(70)
    my_list.add(9)
    my_list.add(100)

    print(my_list)
    print(my_list.index(10))
    # print(my_list.index(101))

    my_list.pop()
    print(my_list)

    my_list.insert(1, 25)
    print(my_list)

    new_lst = my_list.slice(1, 3)
    print(new_lst)
