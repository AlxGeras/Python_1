class Store:
    pass


class OfficeEquipment(Store):

    def __init__(self, name, price, quantity, recipient):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.recipient = recipient
        self.items = [{'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity,
                      'Получатель': recipient}]

    def income(self):
        try:
            quantity = int(input(f'Введите количество: '))
            recipient = input(f'Введите получателя: ')
            item = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': quantity, 'Получатель': recipient}
            self.items.append(item)
            self.items[0]['Количество'] -= quantity
            for i in self.items:
                print(i)


        except ValueError:
            print('Недопустимое значение!')


class Printer(OfficeEquipment):
    def functional(self):
        print('Умеет печатать')


class Scanner(OfficeEquipment):
    def functional(self):
        print('Умеет сканировать')


class Xerox(OfficeEquipment):
    def functional(self):
        print('Умеет копировать')


p = Printer('Hp', 2, 300, 'Склад')
s = Scanner('Canon', 54000, 10, 'Склад')
x = Xerox('Xerox', 7000, 15, 'Склад')
p.functional()
s.functional()
x.functional()
p.income()
p.income()
s.income()
x.income()