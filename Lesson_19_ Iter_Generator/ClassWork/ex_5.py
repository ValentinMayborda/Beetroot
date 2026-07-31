def step_by_step():
    print("Step 1")
    yield 1

    print("Step 2")
    yield 2

    print("Step 3")
    yield 3

g = step_by_step()
print('----Викликаємо генератор----')
print(next(g))

print(next(g))

print(next(g))

import inspect
g2 = step_by_step()
print(inspect.getgeneratorstate(g2))
print(next(g2))
print(inspect.getgeneratorstate(g2))
print(next(g2))
print(inspect.getgeneratorstate(g2))
print(next(g2))
print(inspect.getgeneratorstate(g2))
try:
    print(next(g2))
except StopIteration:
    pass
print(inspect.getgeneratorstate(g2))