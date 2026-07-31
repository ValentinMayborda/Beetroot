# __add__ = протокол для оператора +
# __len__ = протокол для функції len

class Car:
    store_name = "Car Store"

    def __init__(self, year, mark, model, color, price):
        self.year = year
        self.mark = mark
        self.model = model
        self.color = color
        self.price = price

    def __str__(self):
        return f'{self.store_name} - {self.mark} {self.model}: {self.year}, {self.color}, {self.price}$'

    def __repr__(self):
        return f'Car({self.year}, {self.mark}, {self.model}, {self.color}, {self.price})'

    def __eq__(self, other):
        return self.price == other.price

    def __ne__(self, other):
        return self.year != other.year

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def __le__(self, other):
        return self.price <= other.price

    def __ge__(self, other):
        return self.price >= other.price


car_bmw = Car(2022, 'BMW', 'X5', 'red', 100000)
car_audi = Car(2021, 'Audi', 'A4', 'black', 120000)
print(car_bmw)
print(car_audi)
print(repr(car_bmw))
print(car_bmw < car_audi)
print(car_bmw > car_audi)
print(car_bmw == car_audi)
print(car_bmw != car_audi)
print(car_bmw < car_audi)
print(car_bmw > car_audi)
print(car_bmw <= car_audi)
print(car_bmw >= car_audi)

cars = [car_bmw, car_audi]
print(sorted(cars))
