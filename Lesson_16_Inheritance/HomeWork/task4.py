"""Власний виняток

Створіть власний клас винятку CustomException.

Він може успадковуватися від базового класу Exception, але повинен мати додаткову функціональність:

кожне повідомлення про помилку повинно записуватися у файл logs.txt.
Підказка

Використайте метод __init__, щоб розширити функціональність класу та зберігати повідомлення у файл.

"""

class CustomException(Exception):

    def __init__(self, msg):
        self.msg = msg

        with open('logs.txt', 'a', encoding='utf-8') as f:
            f.write(self.msg + '\n')


raise CustomException('Щось пішло не так!')
