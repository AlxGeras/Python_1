class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):

    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):

    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationery):

    def draw(self):
        print('Запуск отрисовки маркером')

My_instrument_1 = Stationery('Общий')

My_instrument_1.draw()

My_instrument_2 = Pen('Ручка')

My_instrument_2.draw()

My_instrument_3 = Pencil('Карандаш')

My_instrument_3.draw()

My_instrument_4 = Handle('Маркер')

My_instrument_4.draw()

