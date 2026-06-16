import sys
import json


# Функція що завантажує файл телефонного записника
def load_file(filename):
    try:
        with open(filename, "r", encoding='utf-8') as file:
            return json.load(file)
            #return data
    except FileNotFoundError as err:
        print("File not found - ", err)
        exit(1)

# Функція що додає новий запис в телефонний довідник *******
def add_entry(pb, first_name, last_name, phone_number, city, state):
    new_contact = {
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_number,
        "city": city,
        "state": state
    }
    pb["contacts"].append(new_contact)

    with open("phonebook.json", "w", encoding="utf-8") as file:
        json.dump(pb, file, indent=4)

# Функція пошуку за іменем
def search_by_firstname(pb, firstname):
    for entry in pb['contacts']:
        if entry['first_name'].lower() == firstname.lower():
            print(f'{firstname} is found --> ', end='')
            for v  in  entry.values():
                print(v, end=' ')
            return
    print('Not found')

# Функція пошуку по прізвищу
def search_by_lastname(pb, lastname):
    for entry in pb['contacts']:
        if entry['last_name'].lower() == lastname.lower():
            print(f'{lastname} is found --> ', end='')
            for v in entry.values():
                print(v, end=' ')
            return
    print('Not found')

# Функція пошуку по імені та прізвищу
def search_by_fullname(pb, firstname, lastname):
    for entry in pb['contacts']:
        if entry['first_name'].lower() == firstname.lower() and entry['last_name'].lower() == lastname.lower():
            print(f'{firstname} {lastname} is found --> ', end='')
            for v in entry.values():
                print(v, end=' ')
            return
    print('Not found')

# Функція пошуку по номеру телефона
def search_by_telephone(pb, phone_number):
    for entry in pb['contacts']:
        if entry['phone_number'] == phone_number:
            print(f'{phone_number} is found --> ', end='')
            for v in entry.values():
                print(v, end=' ')
            return
    print('Not found')

# Функція пошуку по місту
def search_by_city(pb, city):
    for entry in pb['contacts']:
        if entry['city'] == city:
            print(f'{city} is found --> ', end='')
            for v in entry.values():
                print(v, end=' ')
            return
    print('Not found')

# Функція видалення контакту за номером телефону
def del_record(pb, number):
    for entry in pb['contacts']:
        if entry['phone_number'] == number:
            pb['contacts'].remove(entry)

            with open('phonebook.json', 'w', encoding='utf-8') as file:
                json.dump(pb, file, indent=4)

            for v in entry.values():
                print(v, end=' ')
            print('is deleted !!!')
            return

    print(f'{number} - not found!!!')

# Функція оновлення контакту за номером телефону
def update_record(pb, phone_number, first_name, last_name, city, state):
    for entry in pb['contacts']:
        if entry['phone_number'] == phone_number:

            entry['first_name'] = first_name
            entry['last_name'] = last_name
            entry['city'] = city
            entry['state'] = state

            with open('phonebook.json', 'w', encoding='utf-8') as file:
                json.dump(pb, file, indent=4)

            print('Record updated')
            return

    print(f'{phone_number} - not found!!!')

if __name__ == '__main__':
    if len(sys.argv) != 2:
          print('For use: python task2.py phonebook.json')
          sys.exit(1)

    #phonebook = load_file('phonebook.json')
    phonebook = load_file(sys.argv[1])

    while True:
        try:
            print("\n\n***Phonebook application menu***")
            print("1 - Add new entries\n"
                  "2 - Search by first name\n"
                  "3 - Search by last name\n"
                  "4 - Search by full name\n"
                  "5 - Search by telephone number\n"
                  "6 - Search by city or state\n"
                  "7 - Delete a record for a given telephone number\n"
                  "8 - Update a record for a given telephone number\n"
                  "9 - An option to exit the program")
            choice = input("Enter your choice: ")
            match choice:
                case '1':
                    f_name = input("Enter your first name: ")
                    l_name = input("Enter your last name: ")
                    p_number = input("Enter your telephone number: ")
                    city = input("Enter your city: ")
                    state = input("Enter your state: ")
                    add_entry(phonebook, f_name, l_name, p_number, city, state)
                case '2':
                    find_firstname = input("Enter your search name: ")
                    search_by_firstname(phonebook, find_firstname)
                case '3':
                    find_lastname = input("Enter your search last name: ")
                    search_by_lastname(phonebook, find_lastname)
                case '4':
                    find_firstname = input("Enter your search name: ")
                    find_lastname = input("Enter your search last name: ")
                    search_by_fullname(phonebook, find_firstname, find_lastname)
                case '5':
                    find_phonenumber = input("Enter your search telephone number: ")
                    search_by_telephone(phonebook, find_phonenumber)
                case '6':
                    find_city = input("Enter your search city: ")
                    search_by_city(phonebook, find_city)
                case '7':
                    p_number = input("Enter phone number for delete record: ")
                    del_record(phonebook, p_number)
                case '8':
                    p_number = input("Enter your phone number for update record: ")
                    f_name = input("Enter your first name: ")
                    l_name = input("Enter your last name: ")
                    city = input("Enter your city: ")
                    state = input("Enter your state: ")
                    update_record(phonebook, p_number, f_name, l_name, city, state)
                case '9':
                    print("Goodbye!!!")
                    break
                case _:
                    print("Wrong input")

        except ValueError as error:
            print("Wrong input", error)