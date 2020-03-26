number = input('Введите число: ')

i = 0
Max = 0

while i < len(number):
    if int(number[i]) > Max:
        Max = int(number[i])
    i += 1

print('Самое большая цифра в числе: ', Max)
