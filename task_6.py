def int_func(a):
    return a.capitalize()


my_str = input('Введите строку: ')
my_str = my_str.split(' ')

for i, j in enumerate(my_str):
    my_str[i] = int_func(j)

my_str = ' '.join(my_str)

print(my_str)
