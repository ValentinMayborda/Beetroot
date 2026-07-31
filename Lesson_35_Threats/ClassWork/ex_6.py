import threading
import time
class BankAccount:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self, amount):
        # self.lock.acquire()
        # try:
        #     ...
        # finally:
        #     self.lock.release()
        with self.lock:
            current_balance = self.balance
            time.sleep(0.1)
            self.balance = current_balance + amount
            print(f"Deposited: {amount}. New balance: {self.balance}")


account = BankAccount()
def transaction():
    for _ in range(3):
        account.deposit(100)

threads = [threading.Thread(target=transaction) for _ in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"Final balance: {account.balance}")