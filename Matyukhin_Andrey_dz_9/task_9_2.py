class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_asphalt(self, massa, thickness):
        print(f'Требуемая для покрытия дороги '
              f'масса асфальта = {int((self._width * self._length * massa * thickness) / 1000)} т')


road_1 = Road(5000, 20)
road_1.calculate_asphalt(25, 5)
road_1.calculate_asphalt(20, 5)