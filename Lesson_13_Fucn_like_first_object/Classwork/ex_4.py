def greetings(name):  # Зовнішня ф-ція
    def message(msg):  # Внутрішня ф-ція
        return f'{name} - {msg}'
    return message


msg_for_natalia = greetings('Natalia')
msg_for_valentyn = greetings('Valentyn')


print(msg_for_natalia('go to home!'))
print(msg_for_natalia('go to work!'))

print(msg_for_valentyn('do it!'))

