my_str = input('Введите строку: ')

my_list = my_str.split(' ')

for i in my_list:
    if len(i) > 10:
        i = i[:10]
    print(i)