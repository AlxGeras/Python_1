import json

my_list = []
my_dict = {}
average_profit = {}
with open('task_7.txt') as out_f:
    while True:
        line = out_f.readline()
        if line == '\n':
            break
        if line:
            line = line.split(' ')
            my_dict[line[0]] = int(line[2]) - int(line[3])
        else:
            break

n = 0
s = 0

for i in my_dict.values():
    if i > 0:
        s += i
        n += 1

average_profit['average_profit'] = s/n

my_list.append(my_dict)
my_list.append(average_profit)


with open("task_7.json", "w") as write_f:
    json.dump(my_list, write_f)
