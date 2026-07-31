import threading
import time
from concurrent.futures import ThreadPoolExecutor


# Lock(1) - Samophore(1)

semaphore = threading.Semaphore(3)

def fetch_with_limit(url:str)->str:
    with semaphore:
        print(f'[{threading.current_thread().name}] Починаю запит до {url}')
        time.sleep(1)
        return f'ok {url}'

        # semaphore.release () робить with для семафора в кінці

urls = [f'https://api.example.com/item/{i}' for i in range(10)]

with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(fetch_with_limit, urls))

