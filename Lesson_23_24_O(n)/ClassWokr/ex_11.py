def count_chars(text):
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

text = "програмування"
print(count_chars(text))