class Car:
    def __init__(self, name="Безымянный", color="Безцветный", _is_police=False):
        self.name = input("Введите название машины ") if name == "Безымянный" else name
        self.speed = 0
        self.is_police = _is_police
        if self.is_police:
            self.color = "Черный"
        else:
            self.color = input("Введите цвет машины ").title() if color == "Безцветный" else color.title()

    def go(self, sp=None):
        if sp:
            self.speed = sp
        else:
            msg = f'{self.color} {self.name} едит со скоростью {self.speed} км/ч.\nВведите ' \
                  f'новую скорость' if self.speed else f'{self.color} {self.name} cтоит.\nВведите' \
                                                       f' начальную скорость'
            self.speed = int(input(msg))
        print(f'{self.color} {self.name} поехал со скоростью {self.speed} км/ч')

    def stop(self):
        self.speed = 0
        print(f'{self.color} {self.name} остановился')

    def turn(self, direction):
        print(f'{self.color} {self.name} повернул на {direction}')

    def show_speed(self):
        print(f'{self.color} {self.name} едит со скоростью {self.speed} км/ч.'
              if self.speed != 0 else f'{self.color} {self.name} cтоит.')


class TownCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.name = f'городской автомобиль "{self.name}"'

    def show_speed(self):
        print(f'{self.color} {self.name} едит со скоростью {self.speed} км/ч'
              f'{f"." if self.speed <= 60 else f", которая превышает установленную."}'
              if self.speed != 0 else f'{self.color} {self.name} cтоит.')


class SportCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.name = f'спортивный автомобиль "{self.name}"'


class WorkCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.name = f'грузовой автомобиль "{self.name}"'

    def show_speed(self):
        print(f'{self.color} {self.name} едит со скоростью {self.speed} км/ч'
              f'{f"." if self.speed <= 40 else f", которая превышает установленную."}'
              if self.speed != 0 else f'{self.color} {self.name} cтоит.')


class PoliceCar(Car):
    def __init__(self, name):
        super().__init__(name, _is_police=True)
        self.name = f'полицейский автомобиль "{self.name}"'


auto_1 = TownCar("VAZ-2115", "серый")
auto_1.show_speed()
auto_1.go(40)
auto_1.show_speed()
auto_1.go(80)
auto_1.show_speed()
auto_1.turn("лево")
auto_1.stop()
auto_2 = SportCar("Maserati", "красный")
auto_2.show_speed()
auto_2.go(40)
auto_2.show_speed()
auto_2.go(280)
auto_2.show_speed()
auto_2.turn("лево")
auto_2.stop()
auto_3 = WorkCar("КамАз", "желтый")
auto_3.show_speed()
auto_3.go(40)
auto_3.show_speed()
auto_3.go(80)
auto_3.show_speed()
auto_3.turn("право")
auto_3.stop()
auto_4 = PoliceCar("Ford")
auto_4.show_speed()
auto_4.go(40)
auto_4.show_speed()
auto_4.go(80)
auto_4.show_speed()
auto_4.turn("право")
auto_4.stop()
