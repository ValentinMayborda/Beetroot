from multiprocessing import Process
import time
import os


def worker(task_id:int, delay:float):
    pid = os.getpid()
    print(f'[PID {pid}] Task {task_id} started. Delay {delay}')
    time.sleep(delay)
    print(f'[PID {pid}] Task {task_id} finished.')


if __name__ == '__main__':
    parent_pid = os.getppid()
    print(f'Батьківський процес: {parent_pid}')
    processes = [
        Process(target=worker, args=(1, 2.0), name='Worker-1'),
        Process(target=worker, args=(2, 1.0), name='Worker-2'),
        Process(target=worker, args=(3, 1.5), name='Worker-3'),
    ]

    for p in processes:
        p.start()
        print(f'Запущено процес {p.name}, PID: {p.pid}')
    for p in processes:
        p.join()
    print('Всі процеси запущено')