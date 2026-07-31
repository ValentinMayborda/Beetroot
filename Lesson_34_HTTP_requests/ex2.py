# Використати публічне API (наприклад, JSONPlaceholder)
# для отримання списку постів та вивести заголовки постів у консоль.
import requests

# URL API
url = "https://jsonplaceholder.typicode.com/posts"

try:
    # Надсилаємо GET-запит
    response = requests.get(url)

    # Перевіряємо, чи запит успішний
    response.raise_for_status()

    # Отримуємо дані у форматі JSON
    posts = response.json()

    # Виводимо заголовки постів
    print("Список заголовків постів:\n")

    for post in posts[:10]:
        resp = f'{post}, title:{post["title"]}'
        print(resp)


except requests.exceptions.RequestException as e:
    print(f"Помилка при виконанні запиту: {e}")