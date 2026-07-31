import threading
import time

def download_file(file_name, delay) -> None:
    print(f'[{threading.current_thread().name}] Починаю:  {file_name}]')
    time.sleep(delay)
    print(f'[{threading.current_thread().name}] Готово:  {file_name}]')


files = [('photo.jpg', 1), ('video.mp4', 3), ('music.mp3', 2)]
# 1 + 3 + 2 = 6
start = time.perf_counter()
threads = []
for name, delay in files:
    t = threading.Thread(
        target=download_file,
        args=(name, delay),
        name=f"Thread-{name}"
    )
    threads.append(t)
    t.start()

for t in threads:
    t.join()
end = time.perf_counter()
print('Всі файли завантажено!')
print(f'Час виконання (threading): {end - start}с')
#
#
# def download_file_sync(file_name, delay) -> None:
#     print(f"[MAIN] Починаю: {file_name}")
#     time.sleep(delay)
#     print(f"[MAIN] Готово: {file_name}")
#
# start_sync = time.perf_counter()
# for name, delay in files:
#     download_file_sync(name, delay)
# end_sync = time.perf_counter()
# print('Всі файли завантажено!')
# print(f'Час виконання: {end_sync - start_sync}с')