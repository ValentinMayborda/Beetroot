"""Розшир свій клас Stack методом
get_from_stack(e)
який знаходить елемент у стеку та повертає його.
При цьому всі інші елементи повинні залишитися на своїх місцях."""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise ValueError('Стек порожній')

    def is_empty(self):
        return self.items == []

    def get_from_stack(self, target):
        # допоміжний стек
        temp_stack = Stack()

        found = None
        while not self.is_empty():
            item = self.pop()
            temp_stack.push(item)

            if item == target:
                found = item

        # Повертаємо значення в основний стек
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

        if found is None:
            raise ValueError(f'Елемент {target} не знайдено!')
        else:
            return found


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    s = Stack()
    for i in lst:
        s.push(i)

    print(s.get_from_stack(6))
    print(s.items)
