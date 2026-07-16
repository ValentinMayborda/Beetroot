
class Product:
    def __init__(self, product_type:str, name:str, price:float):

        if not isinstance(product_type, str):
            raise ValueError('Product type must be a string')

        if not isinstance(name, str):
            raise ValueError('The name of product must be a string')

        if not isinstance(price, (int, float)):
            raise ValueError('Price must be a number')

        if price <= 0:
            raise ValueError('Price must be more 0')

        self.product_type = product_type
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.product_type} {self.name} {self.price}'

    def __repr__(self):
        return f'{self.product_type} {self.name} {self.price}'


class ProductStore:

    def __init__(self):
        self.income = 0
        self.products = {}


    def add(self, product, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if not isinstance(product, Product):
            raise ValueError("Invalid product")

        if product.name in self.products:
            self.products[product.name]["amount"] += amount
        else:
            self.products[product.name] = {"product": product,  "amount": amount,"store_price": product.price * 1.3}


    def get_product_info(self,product_name):
        if product_name not in self.products:
            raise ValueError(f'Product {product_name} not available')

        product_data = self.products[product_name]
        product = product_data["product"]

        return (product.name, product_data["amount"])

        # За умовою має повертати кортеж з двох значень а не з трьох
        # return (product.name, product_data["amount"], product.price)


    def sell_product(self, product_name, amount):
        if product_name not in self.products:
            raise ValueError(f'Product {product_name} not available')

        product_data = self.products[product_name]

        if product_data["amount"] < amount:
            raise ValueError("Not enough product in stock")

        product_data["amount"] -= amount
        self.income += product_data["store_price"] * amount


    def get_income(self):
        return self.income


    def get_all_products(self):
        return [(name, data['amount']) for name, data in self.products.items()]


    def set_discount(self, identifier, percent, identifier_type='name'):

        if identifier_type not in ("name", "type"):
            raise ValueError("Invalid identifier type")

        if percent < 0 or percent > 100:
            raise ValueError(f'Percent {percent} is out of range')


        for product_data in self.products.values():

            product = product_data["product"]

            if identifier_type == "name" and product.name == identifier:
                product_data["store_price"] *= (1 - percent / 100)

            elif identifier_type == "type" and product.product_type == identifier:
                product_data["store_price"] *= (1 - percent / 100)


p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

s.sell_product('Ramen', 10)

print(s.get_product_info('Ramen'))

s.set_discount("Ramen", 30)

assert s.get_product_info('Ramen') == ('Ramen', 290)