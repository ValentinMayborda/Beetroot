from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

URLS = [
    'https://api.github.com/users/torvalds',
    'https://api.github.com/users/gvanrossum',
    'https://api.github.com/users/antirez',
    'https://api.github.com/users/kennethreitz',
]

def fetch_user(url: str) -> dict:
    resp = requests.get(url, timeout=10)
    user = resp.json()
    return {'name': user.get('name', 'Noname'), 'repos': user.get('public_repos', 0)}


with ThreadPoolExecutor(max_workers=4) as executor:
    futures = {executor.submit(fetch_user, url): url for url in URLS}
    for future in as_completed(futures):
        url = futures[future]
        try:
            data = future.result()
            print(f'{data["name"]}: {data["repos"]} репозиторіїв')
        except Exception as e:
            print(f'Помилка для: {url}: {e!r}')
    # results = list(executor.map(fetch_user, URLS))
    # print(results)