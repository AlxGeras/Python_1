my_list = [1, 2, 'One', 'Two', 1.01, None]

for i, j in enumerate(my_list, 1):
    print(f'Тип {i}-го элемента: {type(j)}')
