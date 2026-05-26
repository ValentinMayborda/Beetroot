num = input('Введіть 6-ти значне число:')

if len(num) != 6 or not num.isdigit():
    print('Некоректний ввід!')
else:
    first_n = int(num[0]) + int(num[1]) + int(num[2])
    second_n = int(num[3]) + int(num[4]) + int(num[5])
    if first_n == second_n:
        print('Це щасливе число')
    else:
        print('Це звичайне число')
