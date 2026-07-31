class Smartphone:
    def __init__(self, model, year, price):
        self.__model = None
        self.__year = None
        self.__price = None
        self.__battery_level = 100
        # Присвоюємо через сеттери
        self.model = model
        self.year = year
        self.price = price

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Model must be a non-empty string")
        self.__model = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if not isinstance(value, int) or not 2010 <= value <= 2026:
            raise ValueError("Year must be a non-negative integer and in the range 2010-2026")
        self.__year = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, (float, int)) or value <= 0:
            raise ValueError("Price must be a positive float")
        self.__price = value

    @property
    def battery(self):
        return self.__battery_level

    def charge(self, amount):
        self.__battery_level = min(100, self.__battery_level + amount)

    def use(self, amount):
        if self.__battery_level - amount < 0:
            raise ValueError("Battery level is too low")
        self.__battery_level -= amount
    def __str__(self):
        return f"Smartphone: {self.__model}, Year: {self.__year}, Price: ${self.__price}, Battery: {self.__battery_level}"

try:
    phone = Smartphone("Iphone", 2026, 1300)
    print(phone)
    phone.use(50)
    print(phone)
    phone.charge(33)
    print(phone)
    phone.battery = 300
    print(phone)
except ValueError as e:
    print('Error is: ', e)

