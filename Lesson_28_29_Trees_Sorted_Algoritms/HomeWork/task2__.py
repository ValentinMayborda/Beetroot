from bs4 import BeautifulSoup


class DomNode:
    def __init__(self, tag, text=""):
        self.tag = tag              # Назва HTML-тега
        self.text = text.strip()    # Текст всередині тега
        self.children = []          # Дочірні вузли
        self.parent = None          # Батьківський вузол

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, level=0):
        indent = "    " * level

        if self.text:
            print(f"{indent}<{self.tag}> : {self.text}")
        else:
            print(f"{indent}<{self.tag}>")

        for child in self.children:
            child.print_tree(level + 1)

    def search(self, tag):
        result = []

        if self.tag == tag and self.text:
            result.append(self.text)

        for child in self.children:
            result.extend(child.search(tag))

        return result


def build_tree(bs_node):
    """
    Рекурсивно будує дерево DomNode
    """

    # Беремо лише текст, який знаходиться безпосередньо в цьому тегу
    text = ""

    for item in bs_node.contents:
        if isinstance(item, str):
            text += item.strip()

    node = DomNode(bs_node.name, text)

    # Рекурсивно додаємо дочірні теги
    for child in bs_node.find_all(recursive=False):
        node.add_child(build_tree(child))

    return node


# ---------------- HTML ----------------

html = """
<html>
    <body>

        <h1>Магазин телефонів</h1>

        <div>

            <p>Apple</p>

            <p>Samsung</p>

            <p>Xiaomi</p>

        </div>

    </body>
</html>
"""

# Парсимо HTML
soup = BeautifulSoup(html, "html.parser")

# Будуємо дерево
root = build_tree(soup.html)

# ---------------- Виведення дерева ----------------

print("DOM-дерево:\n")

root.print_tree()

# ---------------- Пошук ----------------

tag = input("\nВведіть тег для пошуку: ")

result = root.search(tag)

if result:
    print("\nЗнайдений текст:")
    for text in result:
        print(text)
else:
    print("Тег не знайдено.")