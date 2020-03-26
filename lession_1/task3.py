n = int(input('Введите число: '))

size = len(str(n))

result = n + n*10**size + n + n*10**(size*2) + n*10**size + n

print('Результат = ', result)