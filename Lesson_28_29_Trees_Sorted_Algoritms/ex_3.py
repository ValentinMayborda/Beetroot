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
        return child # для зручного ланцюжка

    def get_breadcrumb(self):
        path = []
        current = self
        while current:
            path.append(current.name)
            current = current.parent
        return " > ".join(reversed(path))

    def search(self, name):
        if name == self.name:
            return self
        for child in self.children:
            result = child.search(name)
            if result:
                return result
        return None


root = CategoryNode('Всі категорії', '/')

electronics = root.add_child(CategoryNode('Електроніка', 'electronics'))

phones = electronics.add_child(CategoryNode('Смартфони', 'smartphones'))
laptops = electronics.add_child(CategoryNode('Ноутбуки', 'laptops'))

iphone = phones.add_child(CategoryNode('Apple iPhone', 'iphone'))
samsung = phones.add_child(CategoryNode('Samsung', 'samsung'))

clothes = root.add_child(CategoryNode('Одяг', 'clothes'))
mens = clothes.add_child(CategoryNode('Чоловічий', 'mens'))

found = root.search('Samsung')
print(found.get_breadcrumb())