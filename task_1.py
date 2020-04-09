with open('task_1.txt', "w") as out_f:
    while True:
        my_str = input('Введите данные: ')
        out_f.write(my_str + '\n')
        if my_str == '':
            break
