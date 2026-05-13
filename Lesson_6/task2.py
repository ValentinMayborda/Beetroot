"""Спільні унікальні числа

Згенеруй 2 списки довжиною 10 елементів із випадковими цілими числами від 1 до 10 та створи третій список, який міститиме спільні числа з перших двох списків без повторень.

Обмеження: використовуй лише цикл while та модуль random для генерації чисел."""
import random

list_numbers1 = []
list_numbers2 = []
list_numbers3 = []

i = 0
while i < 10:
    list_numbers1.append(random.randint(1, 10))
    list_numbers2.append(random.randint(1, 10))
    i += 1

print(list_numbers1)
print(list_numbers2)
#list_numbers3 = set(list_numbers1 + list_numbers2) швидка альтернатива, але це вже не список.

for i in list_numbers1:
    if i in list_numbers2 and i not in list_numbers3 :
        #if i not in list_numbers3:
        list_numbers3.append(i)

print(list_numbers3)