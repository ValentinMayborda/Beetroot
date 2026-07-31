import threading
import time

class UnsafeBankAccount:
    def __init__(self):
        self.balance = 0


    def deposit(self, amount):
        current_balance = self.balance
        time.sleep(0.1)
        self.balance = current_balance + amount
        print(f"Поток: {threading.current_thread().name} зробив депозит: {amount}. Новий баланс: {self.balance}")


account = UnsafeBankAccount()
def transaction():
    for _ in range(3):
        account.deposit(100)


threads = []
for i in range(3):
    thread = threading.Thread(target=transaction, name=f"Thread-{i + 1}")
    threads.append(thread)
print(f'Початковий баланс: {account.balance}')
print(f'Запуск транзакцій...')
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f'Фінальний баланс: {account.balance}')

print(f"Очікуваний баланс: {3 * 3 * 100}")