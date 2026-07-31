class Transport:
    def __init__(self, speed, capacity, fuel_type):
        self.speed = speed
        self.capacity = capacity
        self.fuel_type = fuel_type

    def move(self):
        return f"{self.__class__.__name__} рухається зі швидкістю {self.speed} км/год."

    def stop(self):
        return f"{self.__class__.__name__} зупинився."

    def fuel_consumption(self):
        return f"Споживання пального залежить від типу транспорту."


class Car(Transport):
    def __init__(self, speed, capacity, fuel_type, num_doors):
        super().__init__(speed, capacity, fuel_type)
        self.num_doors = num_doors

    def open_trunk(self):
        return "Багажник відкритий."


class Bus(Transport):
    def __init__(self, speed, capacity, fuel_type, ticket_price):
        super().__init__(speed, capacity, fuel_type)
        self.ticket_price = ticket_price

    def collect_fare(self, passengers):
        return f"Зібрано {passengers * self.ticket_price} грн за проїзд."


class Bicycle(Transport):
    def __init__(self, speed, capacity):
        super().__init__(speed, capacity, fuel_type="Немає")

    def fuel_consumption(self):
        return "Велосипед не використовує пальне."


car = Car(120, 5, "Бензин", 4)
bus = Bus(80, 50, "Дизель", 15)
bike = Bicycle(25, 1)

print(car.move(), bus.collect_fare(10), bike.fuel_consumption(), sep="\n")
