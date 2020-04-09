num = input('Введите числа: ')

with open('task_5.txt', "w") as out_f:
    out_f.write(num)

with open('task_5.txt') as out_f:
    line = out_f.readline()
    line = line.split(' ')

s = 0

for i in line:
    s += int(i)

print(s)


