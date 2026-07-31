def outer_function(x):
    y = 10  # ця змінна буде зберігатися в замиканні

    def inner_function():  # inner_function - це замикання
        result = x + y
        print(f'Result is: {result}')
    # Повертаємо inner_function яка є замиканням
    return inner_function


closure = outer_function(5)

closure()
