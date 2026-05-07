number = input('Enter a number: ')

if number.isdigit() and len(number) == 10:
    print('The number is valid')
else:
    print('The number is not valid')