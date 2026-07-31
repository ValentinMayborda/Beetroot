class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"Пробіг цього автомобіля: {self.odometer_reading} км.")

    def update_odometer(self, km):
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print("Ви не можете змінити пробіг на менше значення")

    def increment_odometer(self, km):
        self.odometer_reading += km

my_car = Car('citroen', 'c4')
print(my_car.get_descriptive_name())
# my_car.odometer_reading = 120
# my_car.update_odometer(130)
my_car.increment_odometer(100)
my_car.update_odometer(90)
my_car.read_odometer()
vadym_car = Car('toyota', 'corolla', 2022)
print(vadym_car.get_descriptive_name())