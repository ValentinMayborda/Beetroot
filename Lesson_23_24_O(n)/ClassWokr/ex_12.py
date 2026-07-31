from collections import deque

MAX_LEN = 3

lifo = deque(maxlen=MAX_LEN)

def push(element):
    lifo.appendleft(element)

def pop():
    return lifo.popleft()

push('Volodymyr')
push('Angelina')
push('Valentyn')
push('Ivan')
print(lifo)
# name = pop()
# print(name)
# print(lifo)