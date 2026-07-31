class Product:
    def __init__(self, title, code, count):
        self.title = title
        self.code = code
        self.count = count

    def __str__(self):
        return f"Product: Title: {self.title}, Code: {self.code}, Count: {self.count}"

    def get_title(self):
        return self.title

    def get_code(self):
        return self.code

    def get_count(self):
        return self.count

    def set_count(self, count):
        self.count = count


class Storage:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_products(self):
        return self.products

    def display(self):
        for product in self.products:
            print(product)

    def find_by_code(self, code):
        for product in self.products:
            if product.get_code() == code:
                return product.get_title()
        return None

    def total_items(self):
        return sum(p.count for p in self.products)


potate = Product('Potate', '00332', 2)
tomato = Product('Tomato', '02352', 19)
apple = Product('Apple', '11142', 5)
print(apple)
print(tomato)
storage = Storage()
storage.add_product(potate)
storage.add_product(tomato)
storage.add_product(apple)
storage.add_product(Product('Flowers', '00001', 10))
storage.remove_product(apple)
storage.display()
found = storage.find_by_code('00001')
print('=-=')
print(found)
print(storage.total_items())