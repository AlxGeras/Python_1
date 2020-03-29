my_list = []

print('Для отсановки записи элементов введите input_stop')

key_stop = 'input_stop'
i = 0
a = ''

while True:
    a = input('Введите значение элемента: ')
    if a == key_stop:
        break
    my_list.append(a)
    i += 1

copy_my_list = my_list.copy()

if len(my_list) % 2 == 0:
    for i in range(0, round(len(my_list)/2)):
        buf = my_list[i*2]
        my_list[i*2] = my_list[i*2+1]
        my_list[i * 2 + 1] = buf

if len(my_list) % 2 != 0:
    for i in range(0, round((len(my_list)-1)/2)):
        buf = my_list[i*2]
        my_list[i*2] = my_list[i*2+1]
        my_list[i * 2 + 1] = buf

print('')
print('Записанный список:')
print(copy_my_list)

print('')
print('Преобразованный список список:')
print(my_list)
