"""
Напиши структуру класів, яка реалізує бібліотеку.
Класи:
1) Library
name
books = []
authors = []
2) Book
name
year
author (має бути об’єктом класу Author)
3) Author
name
country
birthday
books = []
Методи класу Library:
new_book(name: str, year: int, author: Author)
group_by_author(author: Author)
group_by_year(year: int)
Додатково:
Усі 3 класи повинні мати зрозумілі методи __repr__ і __str__
У класі Book має бути класова змінна, яка рахує кількість всіх створених книг
"""
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author):
        """створює об’єкт Book
        додає його в список книг бібліотеки
        повертає створену книгу"""

        book = Book(name, year, author)
        self.books.append(book)

        if author not in self.authors:
            self.authors.append(author)

        author.books.append(book)
        return book


    def group_by_author(self, author):
        """повертає список книг заданого автора"""
        return [book for book in self.books if book.author == author]


    def group_by_year(self, year: int):
        """повертає список книг за певний рік"""
        return [book for book in self.books if book.year == year]


    def __str__(self):
        return f"Бібліотека: {self.name}, містить таку кількість книг: {len(self.books)}"

    def __repr__(self):
        return f"Бібліотека = {self.name}, містить таку кількість книг:{len(self.books)}"


class Book:
    count = 0
    def __init__(self, name: str, year: int, author):

        if not isinstance(name, str):
            raise ValueError('Назва має бути рядком')

        if not isinstance(year, int):
            raise ValueError('Рік має бути числом')

        if not isinstance(author, Author):
            raise ValueError('має бути об’єктом класу Author')

        self.name = name
        self.year = year
        self.author = author

        Book.count += 1

    def __str__(self):
        return f'{self.name} {self.year} {self.author.name}'

    def __repr__(self):
        return f"Назва книги={self.name}, рік={self.year}, автор={self.author.name})"


class Author:
    def __init__(self, name:str, country:str, birthday:str):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __str__(self):
        return f"{self.name} {self.country}"

    def __repr__(self):
        return f"Ім'я автора= {self.name}"

author1 = Author("Толкін", "Нова Зеландія", "1955-05-05")
author2 = Author("Роулін", "Велика Британія", "1965-07-31")

lib = Library("Міська бібліотека")

b1 = lib.new_book("Володарь перснів", 1980, author1)
b2 = lib.new_book("Володарь перснів 2", 1981, author1)
b3 = lib.new_book("Гаррі Потер 1", 1997, author2)
b4 = lib.new_book("Гаррі Потер 2", 1998, author2)

print(lib)
print(Book.count)

print(lib.group_by_author(author1))
print(lib.group_by_author(author2))

print(lib.group_by_year(1980))