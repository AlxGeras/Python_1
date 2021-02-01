import time

class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        print(color[0])
        time.sleep(7)
        print(color[1])
        time.sleep(2)
        print(color[2])
        time.sleep(5)

color = ['красный','желтый','зеленый']

Light = TrafficLight

Light.running(color)