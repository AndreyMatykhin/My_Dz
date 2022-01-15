class Cell:
    def __init__(self, num=0, order=20):
        self.num_cells = num
        self.order = order

    def __add__(self, other):
        return Cell(self.num_cells + other.num_cells)

    def __sub__(self, other):
        return Cell(self.num_cells - other.num_cells) if self.num_cells - other.num_cells > 0 else "Вычитание " \
                                                                                                   "невозможно"

    def __mul__(self, other):
        return Cell(self.num_cells * other.num_cells)

    def __floordiv__(self, other):
        return Cell(self.num_cells // other.num_cells) if self.num_cells // other.num_cells > 0 else "Деление " \
                                                                                                     "невозможно"

    def __truediv__(self, other):
        return Cell(self.num_cells // other.num_cells) if self.num_cells // other.num_cells > 0 else "Деление " \
                                                                                                     "невозможно"

    @property
    def make_order(self):
        return f'{"*" * self.order}\n' * (self.num_cells // self.order) + f'{"*" * (self.num_cells % self.order)}'

    def __str__(self):
        name = "".join([k for k, v in globals().items() if v is self])
        print(f'Клетка {name if name else "Result"}:'.center(20, "-"))
        return self.make_order


cell_1 = Cell(155)
cell_2 = Cell(238)
print(cell_1)
print(cell_2)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_2 - cell_1)
print(Cell(12) * Cell(11))
print(cell_2 / cell_1)
print(cell_1 / cell_2)
