from itertools import count

n = int(input('С какого числа генерировать? '))

for el in count(n):
    print(el)
