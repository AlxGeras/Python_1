def del_on_two(a, b):
    try:
        print('Результат деления: ', a / b)
        return 0
    except ZeroDivisionError:
        print('Введите корректные данные.')
        return 1


zde = 1

while zde == 1:
    zde = 0
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    
    zde = del_on_two(a,b)
