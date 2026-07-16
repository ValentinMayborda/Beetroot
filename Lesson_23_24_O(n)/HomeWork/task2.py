"""Напиши програму, яка читає рядок і визначає,
 чи правильно розставлені круглі (),
  квадратні []
   та фігурні {} дужки."""

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


def is_balanced(txt):
    stack = Stack()

    for el in txt:
        if el in '({[':
            stack.push(el)

        elif el == ')':
            if stack.is_empty():
                print("Стек порожній")
                return False
            else:
                top = stack.pop()
                if top != '(':
                    return False
        elif el == '}':
            if stack.is_empty():
                print("Стек порожній")
                return False
            else:
                top = stack.pop()
                if top != '{':
                    return False
        elif el == ']':
            if stack.is_empty():
                print("Стек порожній")
                return False
            else:
                top = stack.pop()
                if top != '[':
                    return False

    if not stack.is_empty():
        return False
    else:
        return True

if __name__ == "__main__":
    #text = '((('
    text = input('Введіть послідовність "({[": ')

    if is_balanced(text):
        print(f"Послідовність {text} -  збалансована")
    else:
        print(f'Послідовність  {text} - не збалансована')
