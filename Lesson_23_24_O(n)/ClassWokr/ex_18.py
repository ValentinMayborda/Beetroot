from collections import deque


class BankQueue:
    def __init__(self):
        self.queue = deque()

    def add_regular_client(self, client_name):
        self.queue.append(client_name)
        print(f"Клієнт {client_name} став у кінець черги")

    def add_vip_client(self, client_name):
        self.queue.appendleft(client_name)
        print(f"VIP Клієнт {client_name} став у початок черги")

    def serve_client(self):
        if self.queue:
            client = self.queue.popleft()
            print(f"Обслуговуємо клієнта: {client}")
            return client
        else:
            print("Черга порожня")
            return None

    def show_queue(self):
        if self.queue:
            print("Черга:")
            for i, client in enumerate(self.queue, 1):
                print(f"{i}. {client}")
        else:
            print("Черга порожня")


bank = BankQueue()

bank.add_regular_client("Іvan Petrenko")
bank.add_regular_client("Volodymyr Vasylyk")
bank.show_queue()

bank.add_vip_client("Angelina Kharkivska")
bank.add_vip_client("Marko Vovchock")
bank.show_queue()
bank.serve_client()
bank.show_queue()
