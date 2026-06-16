"""
Питання:

Чи з'являється новий файл у каталозі, з якого ви запускали скрипти? - ТАК
Що станеться, якщо до імені файлу, переданого у функцію open(), додати шлях до іншого каталогу? - Помилка відкриття
"""

def create_file():
    try:
        with open('myfile.txt', 'w', encoding='utf-8') as myfile:
            myfile.write('Hello file world!\n')
            print('Файл створено!')
    except FileNotFoundError as error:
        print("Файл не створено", error)

def  open_file():
    try:
        with open('myfile.txt', 'r', encoding='utf-8') as myfile:
            content = myfile.read()
            print(content)

    except FileNotFoundError as error:
        print("Не вдалось відкрити файл", error)

if __name__ == '__main__':
    while True:
        your_choice = input('Оберіть дію:\n1 - Створити файл "myfile.txt"\n2 - Відкрити файл "myfile.txt\n3 - Вихід\n')
        if your_choice == '1':
            create_file()
        elif your_choice == '2':
            open_file()
        elif your_choice == '3':
            break
        else:
            print('Не зрозуміла команда, повторіть!')
            continue
