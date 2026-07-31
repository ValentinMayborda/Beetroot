import threading


class Counter:
    def __init__(self):
        self.val = 0

    def increment(self):
        self.val += int(1)


counter = Counter()

threads = [
    threading.Thread(target=lambda: [counter.increment() for _ in range(1_000_000)])
    for _ in range(10)
]
for t in threads:
    t.start()
for t in threads:
    t.join()

expected = 10 * 1_000_000
print(f'Очікувано: {expected}')
print(f'Фактично: {counter.val}')
print(f'Втрачено: {expected - counter.val}')