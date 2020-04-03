def sum_str(a, b):
    b = b.split(' ')
    for i, j in enumerate(b):
        if j == a:
            b.remove(a)
            break
        b[i] = int(j)
    return sum(b)


symbol = 'q'

b = 0

while True:
    print('Для осановки ввода введите символ: ' + symbol)
    my_str = input('Введите числа: ')

    b = b + sum_str(symbol, my_str)

    print(b)

    if symbol in my_str:
        break
