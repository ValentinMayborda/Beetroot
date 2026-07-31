# Напишіть функцію create_bank_account, яка створює три функції для роботи з банківським рахунком:
# deposit (внесення коштів), withdraw (зняття коштів) і get_balance (перегляд балансу).
# Початковий баланс задається параметром initial_balance. Додайте перевірки на помилки.
def create_bank_account(initial_balance=0):
    """
    Створює функції для роботи з банківським рахунком

    Приклад використання:
    >>> deposit, withdraw, get_balance = create_bank_account(1000)
    >>> deposit(500)    # поверне 1500
    >>> withdraw(200)   # поверне 1300
    >>> get_balance()   # поверне 1300
    """
    balance = [initial_balance]

    def deposit(amount):
        if amount <= 0:
            raise ValueError("Сума депозиту повинна бути додатньою")
        balance[0] += amount
        return balance[0]

    def withdraw(amount):
        if amount <= 0:
            raise ValueError("Сума зняття повинна бути додатньою")
        if amount > balance[0]:
            raise ValueError("Недостатньо коштів на рахунку")
        balance[0] -= amount
        return balance[0]

    def get_balance():
        return balance[0]

    return deposit, withdraw, get_balance
