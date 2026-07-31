# MRO
class A:
    def hi(self):
        print('A')


class B(A):
    def hi(self):
        print('B')


class C(A):
    def hi(self):
        print('C')


class D(B, C):
    pass

d = D()
d.hi()

print(D.__mro__)
print(D.mro())
print(A.__dict__)