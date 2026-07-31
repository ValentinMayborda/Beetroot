import threading
import time
import queue


URL_QUEUE = queue.Queue()
RESULT_QUEUE = queue.Queue()
STOP_SIGNAL = None

def producer(urls:list):
    for url in urls:
        URL_QUEUE.put(url)
        print(f'[Producer] додав: {url}]')

    for _ in range(3):
        URL_QUEUE.put(STOP_SIGNAL)

def consumer(worker_id:int):
    while True:
        url = URL_QUEUE.get()
        if url is STOP_SIGNAL:
            print(f'[Worker - {worker_id} завершую')
            break
        try:
            time.sleep(0.5)
            RESULT_QUEUE.put({'url': url, 'status': 200})
        finally:
            URL_QUEUE.task_done()

urls = [f'https://api.example.com/item/{i}' for i in range(10)]

prod = threading.Thread(target=producer, args=(urls,))
cons = [threading.Thread(target=consumer, args=(i,)) for i in range(3)]
prod.start()

for c in cons:
    c.start()
for c in cons:
    c.join()

while not RESULT_QUEUE.empty():
    print(RESULT_QUEUE.get())