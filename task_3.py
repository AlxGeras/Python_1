my_dict = {}
with open('task_3.txt', encoding='utf-8') as out_f:
    while True:
        line = out_f.readline()
        if line == '\n':
            break
        if line:
            line = line.split(' ')
            my_dict[line[0]] = int(line[1].strip())
        else:
            break

print('Следующие сотрудники имеют зарплату меньше 20000 руб.: ')


for key, value in my_dict.items():
    if value < 20000:
        print(key)

print('Средняя зарплата сотрудников составляет: ')
s = 0
for value in my_dict.values():
    s += value

print(s/len(my_dict))