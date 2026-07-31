# Перша вимога - Функція може бути збережена у змінній чи структурі даних
# def mul(a, b):
#     return a * b
#
#
# f = mul  # збреження ф-ції у змінній
#
# result = f(2, 3)
# print(result)
#
# field = {
#     'a': 2,
#     'b': 3,
#     'ops': f
# }
# print(field.get('ops'))
# print(field.get('ops')(5, 6))
# print(field.get('ops')(field.get('a'), field.get('b')))


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
}

numbers = {
    'x': 10,
    'y': 5,
    'operator': operations['*']
}
print(numbers['operator'](numbers['x'], numbers['y']))  # 50
print(operations['+'](numbers['x'], numbers['y']))  # 15
