"""Знайти найдовше слово у введеному реченні (слова розділені пробілами)
 мати батько син донька свято весілля відпустка паралелепіпед
"""
sentence = input('Введіть речення: ')
lst = sentence.split()

long_element = lst[0]
for element in lst:
    if len(long_element) < len(element):
        long_element = element


print(lst)
print(long_element)