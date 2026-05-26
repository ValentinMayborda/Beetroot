"""Створіть просту функцію з назвою favorite_movie, яка приймає рядок із назвою вашого улюбленого фільму.
Функція повинна вивести повідомлення:

Мій улюблений фільм називається {name}"""

def favorite_movie(name:str) -> None:
    """
    :param name:
    :return: None
    """
    print(f'Мій улюблений фільм називається {name}')

favorite_movie('Стражи Галактики')
#a = favorite_movie('Стражи Галактики')
#print(a)
