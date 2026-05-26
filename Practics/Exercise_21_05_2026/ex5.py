"""Дано список рядків. Використовуючи сет, знайдіть і виведіть усі унікальні символи, які
зустрічаються в усіх рядках разом, а потім порахуйте, скільки разів кожен із них з’являється загалом"""

lst = ["hello", "world", "python"]
string = ''.join(lst)
set1 = set(string)
dct = {}

for i in string:
    dct[i] = string.count(i)

#print(string)
print(set1)
print(dct)