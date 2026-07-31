class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    def test(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @radius.deleter
    def radius(self):
        del self._radius

    @property
    def area(self):
        return 3.14 * self._radius ** 2

    @property
    def diameter(self):
        return 2 * self._radius




circle = Circle(5)
print(circle.radius)
print(circle.test())
circle.radius = 10
print(circle.radius)
print(circle.area)
print(circle.diameter)

del circle.radius
circle.radius = 10
print(circle.radius)