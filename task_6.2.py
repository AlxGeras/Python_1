from itertools import cycle

n = int(input('Сколько раз повторить цикл? '))
i = 0
my_list = ['A', 'B', 'C']

for el in cycle(my_list):
    if i // len(my_list) == n:
        break
    print(el)
    i += 1
