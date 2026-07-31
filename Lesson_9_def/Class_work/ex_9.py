def outer():
    x = 'локальна змінна'

    def inner():
        nonlocal x
        x = 'нелокальна змінна х'
        print('Inner function:', x)

    inner()
    print('зовнішня функція:',x)

outer()