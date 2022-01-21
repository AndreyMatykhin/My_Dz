import re


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Date:
    def __init__(self, date):
        try:
            self.date = Date.validator(Date.convert_type(date))
        except TypeError as err:
            print(f'{date} - {err}')
            self.date = None
        except OwnError as err:
            print(err)
            self.date = None

    def __str__(self):
        return f'{str(self.date[0])}-{str(self.date[1]).rjust(2, "0")}-{str(self.date[2]).rjust(2, "0")}' \
            if isinstance(self.date, tuple) else f'{self.date}'

    @classmethod
    def convert_type(cls, date):
        re_date = re.compile(r'^(\d{2})-(\d{2})-(\d+$)')
        if re_date.findall(date):
            return tuple(map(lambda x: int(x), re_date.findall(date)[0]))
        else:
            raise OwnError(
                f'Incorrect date format: {date}.\n Correct format "day-month-year" in numbers without spaces')

    @staticmethod
    def validator(date):
        if ((date[1] in [1, 3, 5, 7, 8, 10, 12] and date[0] <= 31) or \
            (date[1] in [4, 6, 9, 11] and date[0] <= 30) or \
            (date[1] == 2 and date[0] <= 28) or \
            (date[1] == 2 and date[0] == 29 and (date[2] % 4 == 0 and date[2] % 100 != 0 or date[2] % 400 == 0))) \
                and date[2] != 0:
            return date
        else:
            raise OwnError(f'The date '
                           f'"{str(date[0]).rjust(2, "0")}-{str(date[1]).rjust(2, "0")}-{date[2]}" does not exist')


example_1 = Date(34)
print(example_1, example_1.date)
example_2 = Date("15-may-1956")
print(example_2, example_2.date)
example_3 = Date("29-02-2001")
print(example_3, example_3.date)
example_4 = Date("29-02-2000")
print(example_4, example_4.date)
example_5 = Date("39-05-2000")
print(example_5, example_5.date)
example_6 = Date("19-05-0")
print(example_6, example_6.date)
example_7 = Date("22-02-2022")
print(example_7, example_7.date)
