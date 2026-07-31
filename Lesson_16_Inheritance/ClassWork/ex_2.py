class Parent:
    def custom_method(self):
        print('Parent method')

class Child1(Parent):
    def custom_method(self):
        print('Child1 method')


class Child2(Parent):
    def custom_method(self):
        super().custom_method()
        print('Child2 method')


class Child3(Parent):
    def custom_method(self, *args, **kwargs):
        print('Child3 method')


c1 = Child1()
c1.custom_method()

c2 = Child2()
c2.custom_method()

c3 = Child3()
c3.custom_method(1, 3, 5)