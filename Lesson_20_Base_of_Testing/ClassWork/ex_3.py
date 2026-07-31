# Створіть клас SmartFileReader, який дозволяє построково читати великі текстові файли частинами (chunks). Клас повинен:
# 1. Приймати параметри filename (ім’я файлу) і chunk_size (розмір частини в байтах, за замовчуванням 1024) у конструкторі.
# 2. Бути ітерабельним і підтримувати контекстний менеджер (with), щоб автоматично відкривати та закривати файл.
# 3. Читати файл частинами заданого розміру (chunk_size) і повертати рядки по одному за допомогою ітератора.
# 4. Коректно обробляти ситуації, коли частина файлу закінчується посеред рядка (зберігати залишок у буфері для наступного читання).
# 5. Закривати файл після завершення читання або при виході з контекстного менеджера.
# 6. Приклад використання:
# ○ Створити тестовий файл test.txt із вмістом: "Рядок 1\nРядок 2\nРядок 3\nРядок4\nРядок 5".
# ○ Прочитати файл і вивести кожен рядок у форматі "Прочитано: {рядок}".

class SmartFileReader:
    def __init__(self, filename, chunk_size=1024):
        self.filename = filename
        self.chunk_size = chunk_size
        self.file = None
        self.line_buffer = []

    def __enter__(self):
        return self

    def __exit__(self, *args):
        if self.file:
            self.file.close()

    def __iter__(self):
        self.file = open(self.filename, "r", encoding='UTF-8')
        return self

    def __next__(self):
        if self.line_buffer:
            return self.line_buffer.pop(0)

        chunk = self.file.read(self.chunk_size)

        if not chunk:
            self.file.close()
            raise StopIteration

        lines = chunk.split('\n')
        if not chunk.endswith("\n"):
            self.line_buffer = lines[-1:]
            lines = lines[:-1]

        if not lines:
            return next(self)

        self.line_buffer = lines[1:]
        return lines[0]


with open("test.txt", 'w', encoding="UTF-8") as f:
    f.write("Рядок 1\nРядок 2\nРядок 3\nРядок4\nРядок 5")
    
with SmartFileReader(filename='test.txt') as f:
    for line in f:
        print(f'Прочитано {line}')
