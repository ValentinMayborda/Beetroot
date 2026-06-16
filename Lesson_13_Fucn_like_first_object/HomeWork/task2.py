"""Напишіть програму на Python, яка демонструє доступ до функції всередині іншої функції.

Підказка: використайте функцію, яка повертає іншу функцію."""

def first_function():

    def second_function(a, b):

        print('Це внутрішня функція!')
        return a + b

    return second_function

call_second_function = first_function()

print(call_second_function(1, 2))