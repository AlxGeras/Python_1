my_list = ['Один', 'Два', 'Три', 'Четыре']
i = 0
with open('task_4.1.txt', encoding='utf-8') as out_f:
    with open('task_4.2.txt', "w", encoding='utf-8') as out_f2:
        while True:
            line = out_f.readline()
            if line == '\n':
                break
            if line:
                line = line.split(' ')
                line.remove(line[0])
                line.insert(0, my_list[i])
                out_f2.write(' '.join(line))
                i += 1
            else:
                break
