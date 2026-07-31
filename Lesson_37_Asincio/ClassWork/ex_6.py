import asyncio
import time
import random

USE_REAL_NETWORK = False

SAMPLE_PAGES = {
    'Python_(programming_language)': 8500,
    'Asyncio': 3200,
    'Coroutine': 2100,
    'Event_loop': 1800,
    'asyncio.html': 5600,
    # 'https://en.wikipedia.org/wiki/Python_(programming_language)',
    # 'https://en.wikipedia.org/wiki/Multiprocessing',
    # 'https://en.wikipedia.org/wiki/Parallel_computing',
    # 'https://en.wikipedia.org/wiki/Transputer',
    # 'https://en.wikipedia.org/wiki/IEEE_1355',
}

# === СИНХРОННИЙ ВАРІАНТ ===
def fetch_page_sync(name_or_url: str) -> dict:
    try:
        if USE_REAL_NETWORK:
            import requests
            response = requests.get(name_or_url, timeout=10)
            response.raise_for_status()
            html = response.text
            status_code = response.status_code
        else:
            words_count = SAMPLE_PAGES[name_or_url]
            time.sleep(random.Random(name_or_url).uniform(0.3, 0.7))
            html = "word " * words_count
            status_code = 200
        return {
            'url': name_or_url,
            'status': status_code,
            'size': len(html) // 1024,
            'words': len(html.split()),
            'error': None,
        }
    except Exception as e:
        return {
            'url': name_or_url,
            'status': 404,
            'size': 0,
            'words': 0,
            'error': str(e),
        }

def fetch_all_sync(urls: list) -> list:
    return [fetch_page_sync(url) for url in urls]

# === АСИНХРОННИЙ ВАРІАНТ ===
async def fetch_page_async(name_or_url: str) -> dict:
    try:
        if USE_REAL_NETWORK:
            import aiohttp
            async with aiohttp.ClientSession() as session:
                async with session.get(name_or_url, timeout=10) as response:
                    response.raise_for_status()
                    html = await response.text()
                    status_code = response.status
        else:
            words_count = SAMPLE_PAGES[name_or_url]
            await asyncio.sleep(random.Random(name_or_url).uniform(0.3, 0.7))
            html = "word " * words_count
            status_code = 200
        return {
            'url': name_or_url,
            'status': status_code,
            'size': len(html) // 1024,
            'words': len(html.split()),
            'error': None,
        }
    except Exception as e:
        return {
            'url': name_or_url,
            'status': 404,
            'size': 0,
            'words': 0,
            'error': str(e),
        }

async def fetch_all_async(urls: list, max_concurrent: int=5) -> list:
    semaphore = asyncio.Semaphore(max_concurrent)
    async def fetch_with_limit(url):
        async with semaphore:
            return await fetch_page_async(url)
    tasks = [fetch_with_limit(url) for url in urls]
    return await asyncio.gather(*tasks)


def print_results(results: list) -> None:
    for r in results:
        if r['error']:
            print(f' [ERROR] {r["url"]}:  {r["error"]}')
        else:
            print(f' [OK] {r["url"]}: {r["status"]} {r["size"]}kb {r["words"]} words')

if __name__ == '__main__':
    urls = list(SAMPLE_PAGES.keys())
    # urls = list(SAMPLE_PAGES)
    print(f'Завантажуємо {len(urls) }сторінок...'
          f'(режим: {"реальна мережа" if USE_REAL_NETWORK else "локальна імітація"})\n')
    # ---sync
    print('Синхронно - по одній за раз:')
    t = time.perf_counter()
    sync_results = fetch_all_sync(urls)
    sync_time = time.perf_counter() - t
    print_results(sync_results)
    print(f'   Час: {sync_time:.2f}c\n')

    # ---async
    print('Асинхронно - всі сторінки одночасно:')
    t = time.perf_counter()
    async_results = asyncio.run(fetch_all_async(urls, max_concurrent=5))
    async_time = time.perf_counter() - t
    print_results(async_results)
    print(f'   Час: {async_time:.2f}c\n')
    speedup = sync_time / async_time
    print('-' * 50)
    print(f" Sync: {sync_time:.2f}c")
    print(f" Async: {async_time:.2f}c")
    print(f" Speedup: {speedup:.1f}x")