"""
Клас File Context Manager
Створіть власний клас, який поводиться так само, як вбудована функція open().
Також необхідно розширити його функціональність, додавши:
лічильник використань (counter);
логування (logging).
Особливу увагу зверніть на реалізацію методу __exit__(), який повинен відповідати всім вимогам контекстних менеджерів.
"""
import logging

# Логування
logging.basicConfig(filename='file_operations.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')


class FileContextManager:
    counter = 0

    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode, encoding='utf-8')
            FileContextManager.counter += 1
            self._log_operation('Файл відкрито')
            return self.file

        except Exception as err:
            logging.error(f'Не вдалося відкрити файл {self.filename}: {err}')
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            logging.error(f'Помилка під час роботи з файлом {self.filename}: {exc_type.__name__}: {exc_value}')

        if self.file:
            self.file.close()
            self._log_operation('Файл закрито')
        return False

    def _log_operation(self, operation: str) -> None:
        logging.info(f'File {self.filename} - Операція: {operation}')


if __name__ == '__main__':
    with FileContextManager('File_txt.txt', 'w') as file:
        file.write('Hello, world!!!')

    with FileContextManager('File_txt.txt', 'a') as file:
        file.write('\nHello, world!!!')

    with FileContextManager('File_txt.txt', 'r') as file:
        data = file.read()

    try:
        with FileContextManager("test.txt", "w") as file:
            10 / 0
    except ZeroDivisionError:
        print('Помилка виявлена')

    print(FileContextManager.counter)
