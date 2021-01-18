number = input('Введите число: ')
i = 0
maximum = 0

while i < len(number):
    if int(number[i]) > maximum:
        maximum = int(number[i])
    i += 1

print('Самое большая цифра в числе: ', maximum)
