my_list = [7, 5, 5, 3, 3, 2]

print('Для отсановки записи элементов введите input_stop')
print('Исходный список')
print(my_list)

key_stop = 'input_stop'
a = ''

while True:
    a = input('Введите число: ')
    if a == key_stop:
        break
    a = int(a)

    if a in my_list:
        my_list.insert(my_list.index(a)+my_list.count(a), a)
    else:
        my_list.append(a)
        my_list.sort(reverse=True)
    print(my_list)

