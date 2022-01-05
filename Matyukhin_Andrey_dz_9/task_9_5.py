class Stationary:
    def __init__(self, title=None):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationary):
    def draw(self):
        print(f"{self.title + ' ' if self.title else ''}ручка начала писать".capitalize())


class Pencil(Stationary):
    def draw(self):
        print(f"{self.title + ' ' if self.title else ''}карандаш начал рисовать".capitalize())


class Handle(Stationary):
    def draw(self):
        print(f"{self.title + ' ' if self.title else ''}маркер начал рисовать".capitalize())


stat_1 = Stationary()
stat_1.draw()
stat_2 = Pen("перьевая")
stat_2.draw()
stat_3 = Pencil("мой")
stat_3.draw()
stat_4 = Handle("Синий")
stat_4.draw()

