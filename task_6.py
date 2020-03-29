
product = []

a = ''

while True:

    number = int(input('Введите номер товара: '))

    value_1 = input('Ввеите название товара: ')

    value_2 = int(input('Ввеите цену товара: '))

    value_3 = int(input('Ввеите количество товара: '))

    value_4 = input('Ввеите единицу измерения товара: ')

    my_dict = {'название': value_1, 'цена': value_2, 'количество': value_3, 'ед': value_4}

    my_tuple = (number, my_dict)

    product.append(my_tuple)

    if input('Продолжить ввод? (y/n): ') == 'n':
        break

print(product)

my_values_1 = []

my_values_2 = []

my_values_3 = []

my_values_4 = []

for i in product:
    my_values_1.append(i[1].get('название'))
    my_values_2.append(i[1].get('цена'))
    my_values_3.append(i[1].get('количество'))
    my_values_4.append(i[1].get('ед'))

if len(set(my_values_4)) == 1:
    my_values_4 = list(set(my_values_4))

my_dict = {'название':  my_values_1, 'цена': my_values_2, 'количество': my_values_3, 'ед': my_values_4}

print('')
print(my_dict)
