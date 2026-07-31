class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_str: str):
        year, month, day = map(int, date_str.split('-'))
        return cls(year, month, day)  # cls() = Date()

    @classmethod
    def from_tuple(cls, date_tuple: tuple):  # (2024, 3, 15)
        return cls(*date_tuple)

    @staticmethod
    def is_valid_date(year, month, day) -> bool:
        return 1 <= month <= 12 and 1 <= day <= 31

    def __str__(self):
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"


# d1 = Date(2025, 3, 15)   # звичайний конструктор
d2 = Date.from_string("2025-03-15")     # фабрика з рядка
d3 = Date.from_tuple((2025, 3, 15))     # фабрика з кортежу
# print(d1, d2, d3)
# print(type(d1))
print(type(d2))
print(type(d3))
print(Date.is_valid_date(2025, 3, 15))
print(Date.is_valid_date(2025, 13, 15))