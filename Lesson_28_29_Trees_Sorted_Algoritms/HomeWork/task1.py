""" Розширити структуру, яку побудували на уроці, можливістю вставки дерева в наявне дерево та видалення піддерева з дерева, що існує."""

class CategoryNode:
    def __init__(self, name, url_slug):
        self.name = name
        self.url_slug = url_slug
        self.children = []
        self.parent = None

    # Додавання ноди(дитини)
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        return child

    # Вивід іерархії через реверс(список)
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

        #Рекурсивно шукаємо
        for child in self.children:
            result = child.search(name)
            if result:
                return result
        return None

    # Вставка дерева в наявне дерево
    def insert_tree(self, subtree):
        subtree.parent = self
        self.children.append(subtree)

    # Видалення дерева з піддерева
    def remove_subtree(self):
        if self.parent:
            self.parent.children.remove(self)
            self.parent = None

    # Вивід всього дерева
    def print_tree(self, prefix=""):
        print(prefix + "├── " + self.name)
        for child in self.children:
            child.print_tree(prefix + "│   ")



root = CategoryNode("Всі категорії", '/')

electronics = root.add_child(CategoryNode('Електроніка', 'electronics'))

phones = electronics.add_child(CategoryNode('Смартфони', 'smartphones'))
laptops = electronics.add_child(CategoryNode('Ноутбуки', 'laptops'))

iphone = phones.add_child(CategoryNode('Apple iPhone', 'iphone'))
samsung = phones.add_child(CategoryNode('Samsung', 'samsung'))

clothes = root.add_child(CategoryNode('Одяг', 'clothes'))
mens = clothes.add_child(CategoryNode('Чоловічий', 'mens'))


accessories = CategoryNode('Аксесуари', 'accessories')
accessories.add_child(CategoryNode('Чохли', 'cases'))
accessories.add_child(CategoryNode('Зарядні', 'chargers'))

phones.insert_tree(accessories)

found = root.search('Зарядні')
print(found.get_breadcrumb())

root.print_tree()

accessories.remove_subtree()

root.print_tree()