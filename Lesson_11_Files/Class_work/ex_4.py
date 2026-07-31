import collections


def count_words(filename):
    with open(filename, "r", encoding="utf-8") as f:
        words = f.read().lower().split()

    word_count = collections.Counter(words)
    return word_count.most_common(5)


print(count_words('test.txt'))
