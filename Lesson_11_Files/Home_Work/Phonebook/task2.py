import sys
import json


# Функція що завантажує файл телефонного записника
def load_file(filename):
    try:
        with open(filename, "r", encoding='utf-8') as file:
            return json.load(file)

    except FileNotFoundError as err:
        print("File not found - ", err)
        sys.exit(1)
    except json.JSONDecodeError as err:
        print("Invalid JSON:", err)
        sys.exit(1)


# Функція збереження файлу
def save_phonebook(pb, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(pb, file, indent=4)
        print("\nRecord saved")


# Функція для вибору меню
def show_menu():
    print("\n\n***Phonebook application menu***")
    print("1 - Add new entries\n"
          "2 - Search by first name\n"
          "3 - Search by last name\n"
          "4 - Search by full name\n"
          "5 - Search by telephone number\n"
          "6 - Search by city or state\n"
          "7 - Delete a record for a given telephone number\n"
          "8 - Update a record for a given telephone number\n"
          "9 - An option to exit the program\n")
    option = input("Enter your choice: ")
    return option


# Функція що додає новий запис в телефонний довідник
def add_entry(pb):
    while True:
        phone_number = input("Enter your phone number: ")

        try:
            if not phone_number.isdigit() or len(phone_number) != 10:
                raise ValueError("Invalid phone number")
            if any(contact["phone_number"] == phone_number for contact in pb["contacts"]):
                raise ValueError("Phone number already exists")
            break

        except ValueError as err:
            print(f' Error - >', err)

    new_contact = {
        "first_name": input("Enter your first name: "),
        "last_name": input("Enter your last name: "),
        "phone_number": phone_number,
        "city": input("Enter your city: "),
        "state": input("Enter your state: ")
    }
    pb["contacts"].append(new_contact)
    print("New contact added")

    return pb


# Функція пошуку за іменем
def search_by_firstname(pb):
    firstname = input("Enter your search name: ")

    found = False

    for entry in pb['contacts']:
        if entry['first_name'].lower() == firstname.lower():

            print(f'\n{firstname} is found --> ', end='')
            for v in entry.values():
                print(v, end=' ')

            found = True

    if not found:
        print('Not found')


# Функція пошуку по прізвищу
def search_by_lastname(pb):
    lastname = input("Enter your search last name: ")

    found = False

    for entry in pb['contacts']:
        if entry['last_name'].lower() == lastname.lower():

            print(f'\n{lastname} is found --> ', end='')
            for v in entry.values():
                print(v, end=' ')

            found = True

    if not found:
        print('Not found')


# Функція пошуку по імені та прізвищу
def search_by_fullname(pb):
    firstname = input("Enter your search name: ")
    lastname = input("Enter your search last name: ")

    found = False

    for entry in pb['contacts']:
        if entry['first_name'].lower() == firstname.lower() and entry['last_name'].lower() == lastname.lower():

            print(f'\n{firstname} {lastname} is found --> ', end='')
            for v in entry.values():
                print(v, end=' ')

            found = True

    if not found:
        print('Not found')


# Функція пошуку по номеру телефона
def search_by_telephone(pb):
    phone_number = input("Enter your search telephone number: ")

    found = False

    for entry in pb['contacts']:
        if entry['phone_number'] == phone_number:

            print(f'{phone_number} is found --> ', end='')
            for v in entry.values():
                print(v, end=' ')

            found = True

    if not found:
        print('Not found')


# Функція пошуку по місту
def search_by_city(pb):
    city = input("Enter your search city: ")
    for entry in pb['contacts']:
        if entry['city'].lower() == city.lower():
            print(f'{city} is found --> ', end='')
            for v in entry.values():
                print(v, end=' ')
            return
    print('Not found')


# Функція видалення контакту за номером телефону
def del_record(pb):
    number = input("Enter phone number for delete record: ")

    deleted_contact = None

    for contact in pb["contacts"]:
        if contact["phone_number"] == number:
            deleted_contact = contact
            break

    if deleted_contact:
        pb["contacts"] = [c for c in pb["contacts"] if c["phone_number"] != number]

        print(f"Deleted contact is -->", end='')
        for v in deleted_contact.values():
            print(v, end=' ')

    else:
        print(f"{number} - not found!")

    return pb


# Функція оновлення контакту за номером телефону
def update_record(pb):
    while True:
        phone_number = input("Enter your phone number for update record: ")

        try:
            if not phone_number.isdigit() or len(phone_number) != 10:
                raise ValueError("Invalid phone number")
            break
        except ValueError as err:
            print(f' Error - >', err)

    for entry in pb['contacts']:
        if entry['phone_number'] == phone_number:
            entry['first_name'] = input("Enter your first name: ")
            entry['last_name'] = input("Enter your last name: ")
            entry['city'] = input("Enter your city: ")
            entry['state'] = input("Enter your state: ")

            print("Contact updated")
            return pb

    print("Contact not found")
    return pb

if __name__ == '__main__':
    if len(sys.argv) != 2:
          print('For use: python task2.py phonebook.json')
          sys.exit(1)

    phonebook = load_file(sys.argv[1])

    while True:
        choice = show_menu()
        match choice:
            case '1':
                add_entry(phonebook)
                save_phonebook(phonebook, sys.argv[1])
            case '2':
                search_by_firstname(phonebook)
            case '3':
                search_by_lastname(phonebook)
            case '4':
                search_by_fullname(phonebook)
            case '5':
                search_by_telephone(phonebook)
            case '6':
                search_by_city(phonebook)
            case '7':
                del_record(phonebook)
                save_phonebook(phonebook, sys.argv[1])
            case '8':
                update_record(phonebook)
                save_phonebook(phonebook, sys.argv[1])
            case '9':
                print("Goodbye!!!")
                break
            case _:
                print("Wrong input")
