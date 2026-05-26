from decimal import Decimal
import random

total = Decimal('0')
count = 0
num_price = 5

while count < num_price:
    raw_price = Decimal(str(random.uniform(10, 100)))
    print('raw_price', raw_price)
    price = raw_price.quantize(Decimal('0.01'))
    print('Згенерована ціна', price)
    total = total + price
    count +=  1

average = total / num_price if num_price > 0 else Decimal('0')
print(f'Avarage price: {average.quantize(Decimal('0.01'))}')

