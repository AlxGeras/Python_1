def fact(n):
    temp = 1
    for i in range(1, n + 1):
        temp *= i
        yield temp


n = int(input("Укажите факториал какого числа Вы хотели бы узнать?: "))
for i, el in enumerate(fact(n), 1):
    print(f'{i}! = {el}')
