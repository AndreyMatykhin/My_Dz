class Warehouse:
    pass


class OfficeEquipment:
    def __init__(self, manufacturer, model, price):
        self.manufacturer = manufacturer
        self.model = model
        self.price = price


class Printer(OfficeEquipment):
    def __init__(self, manufacturer, model, type_print, format_print, price):
        super().__init__(manufacturer, model, price)
        self.type_print = type_print
        self.format_print = format_print


class Scanner(OfficeEquipment):
    def __init__(self, manufacturer, model, format_scan, scan_resolution, price):
        super().__init__(manufacturer, model, price)
        self.format_scan = format_scan
        self.scn_resolution = scan_resolution


class Xerox(OfficeEquipment):
    def __init__(self, manufacturer, model, type_copy, price):
        super().__init__(manufacturer, model, price)
        self.type_copy = type_copy
