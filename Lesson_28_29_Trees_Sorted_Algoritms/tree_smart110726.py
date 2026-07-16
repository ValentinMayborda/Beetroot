"""реалізувати дерево для побудови ієрархії інтернет-магазину (смартфони → телефони)"""


class CategoryNode:
    def __init__(self, name, url_slug):
        self.name = name
        self.url_slug = url_slug
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        return child

    def get_bradcrumb(self):
        path = []
        current = self
        while current:
            path.append(current.name)

            current = current.parent

        return ' > '.join(reversed(path))



root = CategoryNode('Всі категорії', '/')
electronics = root.add_child(CategoryNode('Електроніка', 'electronics'))
phones = electronics.add_child(CategoryNode('Смартфони', 'smartphones'))
laptops = electronics.add_child(CategoryNode('Ноутбуки', 'laptops'))
iphone = phones.add_child(CategoryNode('Apple iPhone', 'iphone'))
samsung = phones.add_child(CategoryNode('Samsung', 'samsung'))
clothes = root.add_child(CategoryNode('Одяг', 'clothes'))
mens = clothes.add_child(CategoryNode('Чоловічий', 'mens'))

print(samsung.get_bradcrumb())


