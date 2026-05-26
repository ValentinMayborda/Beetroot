"""Створення словника

Створіть функцію з назвою make_country, яка приймає назву країни та її столицю як параметри.
Потім створіть словник із цих двох значень, де:

'name' — ключ для назви країни
'capital' — ключ для столиці

Функція повинна вивести значення словника, щоб переконатися, що вона працює правильно."""

def make_country(name:str, capital:str) -> None:
    """
    :param name:
    :param capital:
    :return: None
    """
    dct = dict(name=name, capital=capital)
    print(dct)

    # for key, value in dct.items():
    #     print(f'{key}: {value}')

make_country('Ukraine', 'Kyiv')