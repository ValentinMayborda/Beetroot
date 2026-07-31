class MyClass:
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class MyClass:
    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    def del_value(self):
        del self._value

    value = property(get_value, set_value, del_value)

