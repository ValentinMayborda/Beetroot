# Створіть функцію для підрахунку частоти символів у рядку, використовуючи словник


def count_chars(text):
    dict_1 = {}
    for char in text:
        dict_1[char] = dict_1.get(char, 0) + 1
    return dict_1

text = "programming"
print(count_chars(text))
