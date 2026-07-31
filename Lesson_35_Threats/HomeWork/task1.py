"""Спільний лічильник (A shared counter)

Створіть клас Counter, який успадковується від класу Thread з модуля threading.
У класі створіть дві глобальні змінні:

counter = 0
rounds = 100000

Тепер реалізуйте метод run().
У ньому зробіть звичайний цикл for, який виконується rounds разів (тобто 100000 ітерацій).
На кожній ітерації збільшуйте значення змінної counter на 1.

Створіть два екземпляри цього потоку.
Запустіть їх методом start().

Після цього дочекайтеся завершення потоків методом join().

Перевірте значення counter.

Здавалося б, воно повинно дорівнювати 200000, чи не так?
Запустіть програму кілька разів і подумайте, чому ви отримуєте саме такий результат."""
import threading


class Counter(threading.Thread):
    counter = 0
    rounds = 100000

    def run(self):
        for i in range(Counter.rounds):
            Counter.counter += 1


thread1 = Counter()
thread2 = Counter()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(thread1.name)
print(thread2.name)
print(Counter.counter)
# Через GIL в мене завжди 200000
