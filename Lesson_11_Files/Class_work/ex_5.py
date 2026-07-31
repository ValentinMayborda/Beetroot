def replace_word(filename, old_word, new_word):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace(old_word, new_word)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)


replace_word('test.txt', ')', '')
