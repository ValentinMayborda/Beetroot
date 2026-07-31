# Створіть клас UserDataGenerator, який генерує задану кількість випадкових тестових даних
# користувачів. Клас повинен:
# 1. Приймати параметр count у конструкторі, який визначає кількість користувачів для генерації.
# 2. Бути ітерабельним, тобто підтримувати використання в циклах for.
# 3. Для кожного користувача генерувати:
#   ○ Унікальний id (починаючи з 1).
#   ○ Ім’я (випадкове з заданого списку: "Іван", "Марія", "Петро", "Олена", "Андрій", "Оксана").
#   ○ Вік (випадкове число від 18 до 70).
#   ○ Електронну пошту (у форматі {ім’я в нижньому регістрі}{випадкове число від 100 до 999}@{домен}, де домен обирається зі списку: "gmail.com", "ukr.net", "outlook.com").
#   ○ Дату реєстрації (випадкова дата в межах останнього року від поточної дати).
# 4. Повертайте дані у вигляді словника для кожного користувача.
# 5. Приклад використання: згенерувати 5 користувачів і вивести їхні дані у форматі "Користувач {id}: {ім’я}, {вік} років".

import random
from datetime import datetime, timedelta


# ── Варіант 1: клас-ітератор ─────────────────────────────────
class UserDataGenerator:
   def __init__(self, count: int):
       self.count = count
       self.current = 0
       self.names = ['Іван', 'Марія', 'Петро', 'Олена', 'Андрій', 'Оксана']
       self.domains = ['gmail.com', 'ukr.net', 'outlook.com']

   def __iter__(self):
       return self

   def __next__(self) -> dict:
       if self.current >= self.count:
           raise StopIteration
       self.current += 1
       name = random.choice(self.names)
       return {
           'id': self.current,
           'name': name,
           'age': random.randint(18, 70),
           'email': f'{name.lower()}{random.randint(100, 999)}@{random.choice(self.domains)}',
           'registered': datetime.now() - timedelta(days=random.randint(1, 365))
       }

for user in UserDataGenerator(3):
   print(f"Користувач {user['id']}: {user['name']}, {user['age']} років")
