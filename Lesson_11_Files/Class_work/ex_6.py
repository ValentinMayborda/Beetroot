def write_user_data():
    print('Enter your data:')
    data = {
        'name': input('Enter your name: '),
        'age': input('Enter your age: '),
        'city': input('Enter your city: ')
    }
    with open('user_data.txt', 'w', encoding='utf-8') as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")

write_user_data()
