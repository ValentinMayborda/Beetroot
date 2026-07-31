import asyncio


async def greet(name: str, delay: float) -> str:
    print(f"[{name}] починаю...")
    await asyncio.sleep(delay)
    print(f'[{name}] готово після {delay}с')
    return f'Привіт від {name}'

async def main():
    coro = greet('Alice', 1.0)
    print(type(coro))
    coro.close()
    result = await greet('Bob', 0.5)
    print(result)
    asyncio.get_running_loop()

asyncio.run(main())
