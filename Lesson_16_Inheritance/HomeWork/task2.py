"""Математик

Реалізуйте клас Mathematician, який буде допоміжним класом для виконання математичних операцій над списками.

Клас не повинен приймати жодних атрибутів і має містити лише такі методи:

square_nums — приймає список цілих чисел і повертає список їх квадратів;
remove_positives — приймає список цілих чисел і повертає список без додатних чисел;
filter_leaps — приймає список років (цілих чисел) і повертає лише високосні роки.
"""

class Mathematician:

    def square_nums(self, lst):
        return [i ** 2 for i in lst]

    def remove_positives(self, lst):
        return [i for i in lst if i < 0]

    def filter_leaps(self, lst):
        return [i for i in lst if i % 4 == 0]


m = Mathematician()

print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90]))
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]