# *args - довільна к-сть позиційних аргументів. (передаються як кортеж)
# **kwargs - довільна к-сть іменованих аргументів. (передаються як словник)
def summ_all(*args):
    print(type(args))
    print(args)
    return sum(args)


print(summ_all(1, 2, 3, 4, 5, 6, 8))


# def print_info(name, age, name, age)
def print_info(**kwargs):
    print('kwargs: ', kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f'{key}: {value}')


print_info(name='Vova', age=38, city='Lviv', hobby='tenis')


# def правильний_порядок(
#         звичайний_позиційний_параметр,
#         параметер_за_замовчування='значення',
#         *args,
#         тільки_іменований,
#         тільки_іменований_з_замовчуванням='значення',
#         **kwargs
# ):
#     pass

def add(a, b, c):
    return a + b + c

values = [1, 2, 3]

print(add(*values))


def greeting(name: str, age: int = 18) -> str:
    """

    :param name:
    :param age:
    :return:
    """
    return f"Привіт, {name}! тобі {age} років."


print(greeting('Vova', 'hello'))
