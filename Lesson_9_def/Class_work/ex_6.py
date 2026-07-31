# lambda аргументи: вираз
# def add(x, y):
#     return x + y


add_lambda = lambda x, y: x + y
print(add_lambda(3, 4))

pairs = [(1, 'b'), (2, 'a'), (3, 'c')]
sorted_pairs = sorted(pairs, key=lambda x: x[0])
print(sorted_pairs)