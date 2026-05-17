""" Обчисліть загальну вартість товарів на складі, де загальна вартість — це сума ціни товару,
 помноженої на кількість цього товару.Код має повернути словник із сумами вартостей для кожного виду товару."""

dct_sum = {} # Словник для суми цін

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

for key in stock:
    dct_sum[key] = prices[key] * stock[key]
    #print(dct_sum[key])

# Вивід словника
for key, value in dct_sum.items():
    print(f'Товар - {key:<10} | вартість: {value:>8}')

#print(dct_sum)
