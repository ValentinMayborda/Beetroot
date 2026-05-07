string = input('Input your string: ')

if len(string) < 2:
    print('Empty string') # або просто print()
else:
    print(string[:2] + string[-2:])
