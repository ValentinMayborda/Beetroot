# print(hash('hello'))
#
# 54 % 11 = 10
# 26 % 11 = 4
# 93 % 11 = 5
# 17 % 11 = 6
# 77 % 11 = 0
# 31 % 11 = 9
# # 54, 26, 93, 17, 77, 31, 44

def simple_hash(text, table_size):
    hash_value = 0
    for char in text:
        hash_value = (hash_value + ord(char)) % table_size
    return hash_value

class SimpleHastTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.table = [[] for _ in range(table_size)]

    def insert(self, key, value):
        index = simple_hash(key, self.table_size)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = simple_hash(key, self.table_size)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None

    def delete(self, key):
        index = simple_hash(key, self.table_size)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                self.table[index].pop(i)
                return
        raise ValueError(f"Key {key} not found in the table")

    def display(self):
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Індекс {i}: {bucket}")

hash_table = SimpleHastTable(10)
students = [
    ("Іван Петренко", "Математика"),
    ("Марія Коваленко", "Фізика"),
    ("Тарас Степаненко", "Геометрія"),
    ("Юрій Мороз", "Географія"),
    ("Вадим Матура", "Біологія"),
]
for name, subject in students:
    hash_table.insert(name, subject)
    hash_value = simple_hash(name, hash_table.table_size)
    print(f"Хеш значення для студента {name} є {hash_value}")

print(hash_table.display())
hash_table.delete("Іван Петренко")
print('Після видалення:')
print(hash_table.display())

print('\nПошук студентів:')
for name, _ in students:
    subject = hash_table.get(name)
    if subject:
        print(f"Студент {name} вивчає предмет {subject}")