import asyncio
import time

async def download(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f'{name} завантажено'

async def main():
    t = time.perf_counter()
    r1 = await download('file-a.zip', 2.0)
    r2 = await download('file-b.zip', 1.0)
    print(r1, r2, f'-- разом {time.perf_counter() - t:.2f}с')

    # =============
    t = time.perf_counter()
    task1 = asyncio.create_task(download('file-a.zip', 2.0))
    task2 = asyncio.create_task(download('file-b.zip', 1.0))
    r1 = await task1
    r2 = await task2
    print(r1, r2, f'-- разом {time.perf_counter() - t:.2f}с')


asyncio.run(main())