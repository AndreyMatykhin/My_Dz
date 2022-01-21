class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:

    def __init__(self):
        self.storage_areas = {}

    def accept(self, other, n=1):
        try:
            if isinstance(n, int) and n > 0:
                for i in range(n):
                    if not (other.__class__.__name__ in self.storage_areas):
                        self.storage_areas[other.__class__.__name__] = []
                    self.storage_areas[other.__class__.__name__].append(other)
            else:
                raise OwnError("Incorrect type of the number of items being moved")
        except OwnError as err:
            print(err)

    def transfer(self, other, n=1):
        try:
            if isinstance(n, int) and n > 0:
                i = 0
                result = []
                for el in self.storage_areas[other.__class__.__name__]:
                    if el.__dict__ == other.__dict__:
                        i += 1
                if i >= n:
                    for i in range(n):
                        if self.storage_areas[other.__class__.__name__][i].__dict__ == other.__dict__:
                            result.append(self.storage_areas[other.__class__.__name__].pop(i))
                    return result
                elif i == 0:
                    return f"Запрошеного для перемещения {other.__class__.__name__} на складе нет"
                else:
                    return f"Запрошеного для перемещения количества {other.__class__.__name__} на складе нет"
            else:
                raise OwnError("Incorrect type of the number of items being moved")
        except OwnError as err:
            print(err)


class OfficeEquipment:
    def __init__(self, manufacturer, model, price):
        self.manufacturer = manufacturer
        self.model = model
        self.price = price


class Printer(OfficeEquipment):
    def __init__(self, manufacturer, model, type_print, price, *features):
        super().__init__(manufacturer, model, price)
        self.type_print = type_print
        self.features = features


class Scanner(OfficeEquipment):
    def __init__(self, manufacturer, model, format_scan, scan_resolution, price):
        super().__init__(manufacturer, model, price)
        self.format_scan = format_scan
        self.scn_resolution = scan_resolution


class Xerox(OfficeEquipment):
    def __init__(self, manufacturer, model, type_copy, price):
        super().__init__(manufacturer, model, price)
        self.type_copy = type_copy


main_warhouse = Warehouse()
main_warhouse.accept(Printer("HP", 'LJ1200', "laser", "A4", 5400), 1)
main_warhouse.accept(Printer("HP", 'LJ1200', "laser", "A4", 5400), 1)
print(main_warhouse.storage_areas)
print(main_warhouse.transfer(Printer("HP", 'LJ1200', "laser", "A4", 5400)))
print(main_warhouse.storage_areas)
print(main_warhouse.transfer(Printer("HP", 'LJ1200', "laser", "A4", 5400), 7))
print(main_warhouse.transfer(Printer("HP", 'LJ1200', "laser", "A4", 5400), -7))
print(main_warhouse.storage_areas)
