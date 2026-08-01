import datetime
from django.http import HttpResponse
import os
import random
from django.shortcuts import render



# def hello_world(request):
#     return HttpResponse("hello world")

def hello_world(request):
    context = {
        'title': "Моя сторінка",
        'message' : 'Привіт світ!',
        'products' : ['Elem1', 'Elem2', 'Elem3']
    }

    return render(request, 'index.html', context)


def current_time(request):
    now = datetime.datetime.now()
    html = f'<h1>Поточний час</h1><p>Зараз:{now.strftime('%Y-%m-%d %H:%M:%S')}</p>'
    return HttpResponse(html)


# Створіть view, яка приймає ім'я з URL та відображає вітання.
# http://127.0.0.1:8000/greet/volodymyr/

def greet(request, username):
    return HttpResponse(f'Hello, {username}')


# Створіть view для простого калькулятора,
# який приймає два числа і операцію з URL.

def calculator(request, num1, operation, num2):
    result = None
    if operation == 'plus':
        result = num1 + num2
    elif operation == 'minus':
        result = num1 - num2
    elif operation == 'mult':
        result = num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            result = 'Ділення на ноль!'

    return HttpResponse(f'Результат {num1} {operation} {num2} = {result}')


# Створіть view, яка відображає список файлів у поточній директорії проекту.
# Передбачити можливість відображе для конкретної директорії

def show_files(request, directory='.'):
    try:

        files = os.listdir(directory)

        html = f"Файли у директорії {directory} <ul>"

        for file in files:
            if os.path.isfile(file):
                file_type = 'file'
            else:
                file_type = 'dir'

            html += f'<li> {file}:{file_type}</li>'

        html += '</ul>'

        return HttpResponse(html)

    except Exception as e:
        return HttpResponse(f'Помилка: {e}')

# Створіть view, яка відображає всі HTTP-заголовки
# з запиту користувача.

def show_headers(request):
    headers = request.META  # Cловник
    html = ''
    for key, value in headers.items():
        if key.startswith('HTTP_'):
            header_name = key[5:].replace('_', '-').title()
            html += f'{header_name} : {value}<br>'

    #print(headers)
    return HttpResponse(html)

# Створіть view, яка генерує випадкове число в заданому діапазоні.
def random_number(request,min_num=1,max_num=100):
    number = random.randint(min_num, max_num)
    return HttpResponse(f'Випадкове число {number}')
