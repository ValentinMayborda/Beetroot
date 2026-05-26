from decimal import Decimal
import random

balance = Decimal('100.00')
cost_per_try = Decimal('10.00')
secret = random.randint(1, 50)

while balance >= cost_per_try:
    print(f'Ваш баланс: {balance}')

    user_input = input('Вгадайте число від 1 до 50 (або  Exit для виходу): ')
    if user_input.lower() == 'exit':
        break

    if not user_input.isdigit():
        print("Некоретний відвід")
        continue

    guess = int(user_input)
    if not (1 <= guess <= 50):
        print("Число має бути в діапазоні!!!")
        continue

    balance -= cost_per_try

    if guess == secret:
        prize = Decimal('200.00')
        balance += prize
        print(f'Ви агадали! Виграш : {prize}')
        break
    elif guess < secret:
        print("Більше")
        continue
    else:
        print("Менше")


print("Фінальний баланс", balance)
