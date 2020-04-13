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


Car_1 = TownCar(70, 'красный', 'BMW', None)

print(Car_1.speed)
print(Car_1.color)
print(Car_1.name)
print(Car_1.is_police)
Car_1.go()
Car_1.turn('влево')
Car_1.show_speed()
Car_1.stop()

print('------------------------')
Car_2 = WorkCar(60, 'синий', 'Heyndai', None)

print(Car_2.speed)
print(Car_2.color)
print(Car_2.name)
print(Car_2.is_police)
Car_2.go()
Car_2.turn('вправо')
Car_2.show_speed()
Car_2.stop()

print('------------------------')
Car_3 = SportCar(160, 'черный', 'Ferrari', None)

print(Car_3.speed)
print(Car_3.color)
print(Car_3.name)
print(Car_3.is_police)
Car_3.go()
Car_3.turn('влево')
Car_3.show_speed()
Car_3.stop()

print('------------------------')
Car_4 = PoliceCar(60, 'черно-белый', 'УАЗ', True)

print(Car_4.speed)
print(Car_4.color)
print(Car_4.name)
print(Car_4.is_police)
Car_4.go()
Car_4.turn('вправо')
Car_4.show_speed()
Car_4.stop()
