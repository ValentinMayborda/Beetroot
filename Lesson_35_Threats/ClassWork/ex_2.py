import threading
import time

class WorkerThread(threading.Thread):
    def __init__(self, task_id: int, data: list):
        super().__init__(name=f"Worker-{task_id}")
        self.task_id = task_id
        self.data = data
        self.result = None

    def run(self):
        print(f"[{self.name}] обробляю {len(self.data)} елементів...")
        time.sleep(1)
        self.result = sum(self.data)
        print(f'{self.name}: готово! Сума = {self.result}')

workers = [
    WorkerThread(1, [1, 2, 3, 4, 5]),
    WorkerThread(2, [10, 20, 30]),
    WorkerThread(3, list(range(100))),
]
for worker in workers:
    worker.start()

for worker in workers:
    worker.join()

total = sum(w.result for w in workers)
print(f'Загальна сума: {total}')