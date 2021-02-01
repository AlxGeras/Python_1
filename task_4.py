class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        self._direction = direction
        print(f'Машина повернула {self._direction}')

    def show_speed(self):
        print(f'Скорость равна {self.speed}')

class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости!')
        else:
            print(self.speed)

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости!')
        else:
            print(self.speed)

class SportCar(Car):
    pass

class PoliceCar(Car):
    pass

car_1 = TownCar(50, 'красный', 'BMW', None)

print(car_1.speed)
print(car_1.color)
print(car_1.name)
print(car_1.is_police)
car_1.go()
car_1.turn('влево')
car_1.show_speed()
car_1.stop()

print('------------------------')
car_2 = WorkCar(60, 'синий', 'Heyndai', None)

print(car_2.speed)
print(car_2.color)
print(car_2.name)
print(car_2.is_police)
car_2.go()
car_2.turn('вправо')
car_2.show_speed()
car_2.stop()

print('------------------------')
car_3 = SportCar(160, 'черный', 'Ferrari', None)

print(car_3.speed)
print(car_3.color)
print(car_3.name)
print(car_3.is_police)
car_3.go()
car_3.turn('влево')
car_3.show_speed()
car_3.stop()

print('------------------------')
car_4 = PoliceCar(60, 'черно-белый', 'УАЗ', True)

print(car_4.speed)
print(car_4.color)
print(car_4.name)
print(car_4.is_police)
car_4.go()
car_4.turn('вправо')
car_4.show_speed()
car_4.stop()
