"""Напиши програму, яка читає послідовність символів і виводить її у зворотному порядку,
 використовуючи власну реалізацію класу Stack."""


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
        #return len(self.items) == 0
        return self.items == []


if __name__ == "__main__":

    stack = Stack()

    text = 'Valentyn'
    for char in text:
        stack.push(char)

    result = []
    while not stack.is_empty():
        result.append(stack.pop())

    #print(result)
    print(''.join(result))
