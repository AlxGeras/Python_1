from sys import argv

productivity, rate, premium = argv[1:]

print('Выработка в часах: ', productivity)
print('Ставка в час: ', rate)
print('Премия: ', premium)
print(f'Зарплата: {float(productivity)*float(rate)+float(premium)}')
