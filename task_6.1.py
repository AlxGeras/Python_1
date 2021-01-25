from itertools import count

n = int(input('С какого числа генерировать? '))

k = int(input('На каком элементе прервать генерацию? '))

for el in count(n):
    print(el)
    if el == k:
        break
