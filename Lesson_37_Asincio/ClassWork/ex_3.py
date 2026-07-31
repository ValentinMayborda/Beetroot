import asyncio


async def set_after_delay(future: asyncio.Future, delay: float, value):
    await asyncio.sleep(delay)
    future.set_result(value)


async def main():
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    asyncio.create_task(set_after_delay(future, 1.5, 'Готово!'))
    print('Чекаємо результату...')
    result = await future
    print(f'Отримали: {result}')

asyncio.run(main())