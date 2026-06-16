# Маємо список людей (ім'я, дата_народження).
# Для кожного порахувати, скільки днів лишилось до найближчого дня народження;
# визначити, хто святкує наступним;
# вивести список, відсортований за віком.
from datetime import date

people = [
    ("Оля", date(1995, 7, 20)),
    ("Іван", date(2000, 6, 10)),
    ("Марія", date(1988, 12, 1)),
    ("Петро", date(2002, 6, 7)),
]

today = date.today()
#print(today)

def days_untill_birthday(birthday, ref):
    next_birthday = birthday.replace(year=ref.year);
    #print(next_birthday)
    if next_birthday < ref:
        next_birthday = next_birthday.replace(year=ref.year+1)
    return (next_birthday - ref).days


def age(birth, ref):
    years = ref.year - birth.year
    if (ref.month, ref.day) < (birth.month, birth.day):
        years -= 1
    return years

upcoming = []

for name, birth in people:
    days = days_untill_birthday(birth,today)
    