"""Створіть програму, яка отримує на вхід якесь речення (рядок) і повертає словник (dict),
 що містить усі унікальні слова як ключі та кількість їх появ у реченні як значення."""

sentence = input("Введіть речення: ")
lst = list(sentence.split())
dct = {}

for key in lst:
    if key not in dct:
        dct[key] = lst.count(key)

#print(sentence)
#print(lst)
print(dct)
