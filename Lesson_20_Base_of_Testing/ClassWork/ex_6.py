# Задача 3: Ітератор для генерації діапазону дат
# Створіть клас DateRange, який генерує послідовність дат від початкової до кінцевої. Клас повинен:
# 1. Приймати параметри start_date (початкова дата) і end_date (кінцева дата) у конструкторі.
# 2. Бути ітерабельним, генеруючи дати по одній, збільшуючи поточну дату на 1 день за кожну ітерацію.
# 3. Зупиняти генерацію, коли поточна дата перевищує кінцеву дату.
# 4. Мати метод weekdays_only(), який повертає ітератор, що включає лише робочі дні (понеділок–п’ятниця, виключаючи суботу та неділю).
# 5. Приклад використання:
# ○ Згенерувати всі дати від 1 січня 2024 року до 10 січня 2024 року і вивести їх у форматі "YYYY-MM-DD".
# ○ Згенерувати лише робочі дні за той самий період і вивести їх у форматі "YYYY-MM-DD".

from datetime import date, timedelta


class DateRange:

    def __init__(self, start_date: date, end_date: date):
        self.start_date = start_date
        self.end_date = end_date
        self.current_date = start_date

    def __iter__(self):
        self.current_date = self.start_date  # скидаємо при кожному iter()
        return self

    def __next__(self) -> date:
        if self.current_date > self.end_date:
            raise StopIteration
        d = self.current_date
        self.current_date += timedelta(days=1)
        return d

    def weekdays_only(self):
        return filter(lambda d: d.weekday() < 5, self)

    def business_days(self, holidays: list = None):
        holidays = set(holidays or [])

        return filter(
            lambda d: d.weekday() < 5 and d not in holidays,
            self
        )


start = date(2024, 1, 1)
end = date(2024, 1, 10)
print('Всі дні:')
for d in DateRange(start, end):
    print(d.strftime('%Y-%m-%d'), end=' ')

print('\n\nТільки робочі дні:')
for d in DateRange(start, end).weekdays_only():
    print(d.strftime('%Y-%m-%d'), end=' ')
