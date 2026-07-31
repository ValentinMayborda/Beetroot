def add(a, b):
    return a + b

# Позиційні аргументи
print(add(3, 5))


def introduce(name, age):
    print(f'My name is {name}, i"m {age} old')


# Іменовані аргументи
introduce(age=38, name='Vova')


def describe_person(name, age, city):
    print(f'{name}, {age} years, from city: {city}')


describe_person('Vova', 38, city='Lviv')


def full_name(first_name, last_name, middle_name=''):
    print(f'Hello! {first_name}, {last_name}, {middle_name}')


full_name('Vova', 'Vasylyk', 'Mykhailovych')


def greet(name='Гість'):
    print(f'Hello, {name}!')


greet()
greet('Vova')


