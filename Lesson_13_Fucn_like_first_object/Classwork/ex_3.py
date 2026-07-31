# Функція може бути повернена з функції як результат

def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def math_operation(operator: str):
    if operator == "*":
        return mul
    elif operator == "+":
        return add
    else:
        raise ValueError('Operator not supported')


f_mul = math_operation('*')
print(f_mul)
res = f_mul(2, 4)
print(res)