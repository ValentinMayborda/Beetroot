import datetime

class Node:
    def __init__(self, url, title, timestamp=None):
        self.url = url
        self.title = title
        self.timestamp = timestamp
        self.prev = None


class BrowserHistory:
    def __init__(self):
        self.current = None
        self.size = 0

    def visit_page(self, url, title, timestamp=None):  # O(1)
        new_page = Node(url, title, timestamp)
        if self.current:
            new_page.prev = self.current

        self.current = new_page
        self.size += 1
        return new_page

    def go_back(self, steps=1):  # O(steps)
        if not self.current:
            return None
        page = self.current
        for _ in range(steps):
            if page.prev:
                page = page.prev
            else:
                break
        self.current = page
        return page

    def clear_history(self):  # O(1)
        self.current = None
        self.size = 0

    def get_history(self, max_items=None):  # O(n)
        history = []
        page = self.current
        count = 0
        while page and (max_items is None or count < max_items):
            history.append(page)
            page = page.prev
            count += 1
        return history

    def search_history(self, query):  # O(n)
        results = []
        page = self.current
        while page:
            if (query.lower() in page.url.lower() or
                    (page.title and query.lower() in page.title.lower())):
                results.append(page)
            page = page.prev
        return results



if __name__ == "__main__":
    browser = BrowserHistory()
    browser.visit_page("https://www.google.com", "Google", datetime.datetime.now())
    browser.visit_page("https://www.wikipedia.org", "Wikipedia", datetime.datetime.now())
    browser.visit_page("https://www.youtube.com", "YouTube", datetime.datetime.now())
    browser.visit_page("https://www.facebook.com", "Facebook", datetime.datetime.now())
    browser.visit_page("https://www.instagram.com", "Instagram")

    print('Поточна історія (від найновішої до найстарішої): ')
    for i, page in enumerate(browser.get_history()):
        print(f"{i+1}. {page.url} - {page.title}")

    back_page = browser.go_back(2)
    print(f"Повернуто на сторінку: {back_page.url} - {back_page.title}")

    print('Оновлена історія після переходу назад: ')
    for i, page in enumerate(browser.get_history()):
        print(f"{i + 1}. {page.url} - {page.title}")

    browser.visit_page("https://www.youtube.com", "YouTube", datetime.datetime.now())

    print('Кінцева історія після додавання нової сторінки: ')
    for i, page in enumerate(browser.get_history()):
        print(f"{i + 1}. {page.url} - {page.title}")

    search_results = browser.search_history('youtube')

    print('Результат пошуку за запитом : ')
    for i, page in enumerate(search_results):
        print(f"{i + 1}. {page.url} - {page.title}. Timestamp: {page.timestamp}")

