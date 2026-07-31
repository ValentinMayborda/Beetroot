import threading

import time

config_ready = threading.Event()
shutdown = threading.Event()

def get_config():
    print('[Config] Завантаження конфігурації')
    time.sleep(2)
    print('[Config] Конфіг готовий...')
    config_ready.set()


def worker(worker_id:int):
    print(f'[Worker- {worker_id}] Чекаю на конфіг....')
    config_ready.wait()
    print(f'[Worker- {worker_id}] Конфіг отримано, починаю роботу...')

    while not shutdown.is_set():
        time.sleep(0.5)
    print(f'[Worker- {worker_id}] Завершую роботу')


threads = [threading.Thread(target=get_config())]
threads += [threading.Thread(target=worker, args=(i,)) for i in range(3)]

for t in threads:
    t.start()

time.sleep(5)
shutdown.set()

for t in threads:
    t.join()

