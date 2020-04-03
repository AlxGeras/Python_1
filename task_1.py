def del_on_two(*args):
    return args[0]/args[1]


zde = 1

while zde == 1:
    zde = 0
    a = int(input('Введите первое число: '))

    b = int(input('Введите второе число: '))

    try:
        print('Результат деления: ', del_on_two(a, b))
    except ZeroDivisionError:
        print('Введите корректные данные.')
        zde = 1
