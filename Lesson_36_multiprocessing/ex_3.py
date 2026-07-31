import time
from multiprocessing import Process, Queue

def producer(q: Queue, items: list, consumers_count: int) -> None:
    for item in items:
        print(f'[Producer] відправляю: {item}')
        q.put(item)

    for _ in range(consumers_count):
        q.put(None)

def consumer(q: Queue, name: str):
    while True:
        item = q.get()
        time.sleep(0.2)
        if item is None:
            print(f'[{name}] завершує роботу')
            break
        result = item ** 2
        print(f"[{name}] {item} ** 2 = {result}")

if __name__ == '__main__':
    q = Queue()
    data = list(range(1, 9))
    consumers_count = 2
    p_prod = Process(target=producer, args=(q, data, consumers_count))
    p_cons1 = Process(target=consumer, args=(q, "Consumer-1"))
    p_cons2 = Process(target=consumer, args=(q, "Consumer-2"))
    processes = [p_prod, p_cons1, p_cons2]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print('Усі процеси завершені!')