x = 50


def func():
    global x
    print('x is ', x)
    x = 2
    print('Change global x to ', x)


if __name__ == "__main__":
    func()
    print('Value of x is ', x)

