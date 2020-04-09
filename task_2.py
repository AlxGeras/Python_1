my_list = []
with open('task_2.txt', encoding="utf-8") as out_f:
    while True:
        line = out_f.readline()
        if line:
            if line == '\n':
                my_list.append(0)
            else:
                my_list.append(len(line.split(' ')))
        else:
            break

print('Количество строк в файле равно ', len(my_list))

for i, quantity in enumerate(my_list, 1):
    print(f'Количество слов в {i}-й строке равно {quantity}')


