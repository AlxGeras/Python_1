my_dict = {}

with open('task_6.txt') as out_f:
    while True:
        line = out_f.readline()
        if line == '\n':
            break
        if line:
            line = line.split(' ')
            if line[1] != '—':
                lection = int(line[1][:line[1].find('(л)')])
            else:
                lection = 0
            if line[2] != '—':
                practic = int(line[2][:line[2].find('(пр)')])
            else:
                practic = 0
            if line[3] != '—':
                lab = int(line[3][:line[3].find('(лаб)')])
            else:
                lab = 0
            my_dict[line[0][:len(line[0])-1]] = lection + practic + lab

        else:
            break


print(my_dict)




