import threading
import time

def background_logger():
    while True:
        print(f"[LOG] Система працює... {time.strftime('%H:%M:%S')}")
        time.sleep(2)


logger = threading.Thread(target=background_logger, daemon=True)
logger.start()
print('Основна програма виконує роботу...')
time.sleep(7)
print('Основна програма завершена - daemon теж зупиниться автоматично.')
