# Прочитати текстовий файл, порахувати
# частоту слів (без урахування регістру й розділових знаків).
# Вивести топ-5 слів,
# кількість унікальних слів і слова, що зустрічаються рівно один раз (через генератор множини).
import string
from email.contentmanager import set_text_content

text = """Python is great. Python is simple and Python is powerful.
Learning Python is fun, and practice makes learning better."""

with open('text.txt', 'w') as file:
    file.write(text)

with open('text.txt', 'r') as file:
    content = file.read().lower()

# Видаляє всі розділові знаки # punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
words = content.translate(str.maketrans('', '', string.punctuation)).split()
print(words)

word_dict = {}
for word in words:
    word_dict[word] = word_dict.get(word, 0) + 1

top_5_words = sorted(word_dict.items(), key=lambda pair:pair[1], reverse=True)[:5]
#print(top_5_words)

#print(word_dict)

count: object
for word, count in top_5_words:
    print(word, count)


uniq_words = set(words)
print(len(uniq_words))


ones_word = {word for word in words if words.count(word) == 1}
print(ones_word)



