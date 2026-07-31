import asyncio
import random
# import queue => queue.Queue

async def producer(queue: asyncio.Queue, name: str, count: int) -> None:
    for i in range(count):
        item = {'producer': name, 'value': random.randint(1, 100)}
        await queue.put(item)
        print(f'[{name}] поклав: {item["value"]}')
        await asyncio.sleep(random.uniform(0.2, 0.8))
    print(f'{[name]} Завершив роботу!')


async def consumer(queue: asyncio.Queue, name: str) -> None:
    while True:
        try:
            item = await asyncio.wait_for(queue.get(), timeout=2)
            result = item['value'] ** 2
            print(f'[{name}] обробив {item["value"]}^2 = {result}')
            queue.task_done()
            await asyncio.sleep(0.3)
        except asyncio.TimeoutError:
            print(f'[{name}] черга порожня, завершуємо роботу')
            break

async def main():
    queue = asyncio.Queue(maxsize=10)
    producers = [asyncio.create_task(producer(queue, f"P{i}", 5)) for i in range(2)]
    consumers = [asyncio.create_task(consumer(queue, f"C{i}")) for i in range(3)]
    await asyncio.gather(*producers)
    await queue.join()
    for c in consumers:
        c.cancel()

asyncio.run(main())
