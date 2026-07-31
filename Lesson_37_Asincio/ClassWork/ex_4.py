# gather(*coroutines)
import asyncio
import time

def work_sync(i):
    time.sleep(i)
    print(i)


async def work_async(i):
    await asyncio.sleep(1)
    print(i)


async def main_sync():
    tasks = [asyncio.create_task(work_async(i)) for i in range(3)]
    await asyncio.gather(*tasks)

print('Синхронно (по черзі):')
start = time.time()
for i in range(3):
    work_sync(i)
print(f'Час виконання: {time.time() - start:.2f}с\n')

print('Асинхронно (одночасно)')
start = time.time()
asyncio.run(main_sync())
print(f'Час виконання: {time.time() - start:.2f}с\n')