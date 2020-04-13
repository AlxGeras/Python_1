class Road:
    def __init__(self, length, width):
        self._length = int(length)
        self._width = int(width)
        self.__thickness = 5
        self.__mass_per_metr = 25

    def mass(self):
        value_of_mass = (f'Масса асфальта равна: {self._length*self._width*self.__thickness*self.__mass_per_metr} т.')
        return value_of_mass

My_road = Road(666, 13)

print(My_road.mass())