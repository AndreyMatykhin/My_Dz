import re


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class ComplexNumber:
    def __init__(self, date):
        try:
            if isinstance(date, str):
                date = ComplexNumber.convert_type(date)
                self.real = date[0]
                self.imag = date[1]
            else:
                raise OwnError(f"Type {date} – {type(date)}. It's incorrect type")
        except OwnError as err:
            print(err)
            self.real = 0
            self.imag = 0

    def __str__(self):
        name = "".join([k for k, v in globals().items() if v is self])
        return f'{name if name else "Result"}: ' \
               f'{self.real if self.real != 0 else ""}' \
               f'{"+" if self.imag > 0 and self.real != 0 else ""}' \
               f'{f"{self.imag}j" if self.imag != 0 else ""}' if self.real or self.imag else f'No number'

    @classmethod
    def convert_type(cls, date):
        if re.compile(r'[^j\d.+-]').findall(date):
            raise OwnError(f'{date} - incorrect format of complex number: '
                           f'A complex number consists of real and imaginary parts without spaces.'
                           f' For example: "4-6j", "34j-56", "-65j", "55"')
        else:
            dig_list = [match.group() for match in re.finditer(r"([-+]{0,1}\d+([.]{0,1})+\d{0,}j{0,1})", date)]
            return [sum(float(el) for el in dig_list if el[-1] != "j"),
                    sum(float(el[:-1]) for el in dig_list if el[-1] == "j")]

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            real = self.real + other.real
            imag = self.imag + other.imag
            return ComplexNumber(f'{real if real != 0 else ""}{"+" if imag > 0 and real != 0 else ""}'
                                 f'{f"{imag}j" if imag != 0 else ""}')
        elif isinstance(other, str):
            return self + ComplexNumber(other)
        else:
            raise OwnError(f'{other} - incorrect type')

    def __iadd__(self, other):
        if isinstance(other, ComplexNumber):
            self.real = self.real + other.real
            self.imag = self.imag + other.imag
            return self
        elif isinstance(other, str):
            return self + ComplexNumber(other)
        else:
            raise OwnError(f'{other} - incorrect type')

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            real = self.real * other.real - self.imag * other.imag
            imag = self.real * other.imag + self.imag * other.real
            return ComplexNumber(f'{real if real != 0 else ""}{"+" if imag > 0 and real != 0 else ""}'
                                 f'{f"{imag}j" if imag != 0 else ""}')
        elif isinstance(other, str):
            return self * ComplexNumber(other)
        else:
            raise OwnError(f'{other} - incorrect type')

    def __imul__(self, other):
        if isinstance(other, ComplexNumber):
            real = self.real * other.real - self.imag * other.imag
            imag = self.real * other.imag + self.imag * other.real
            self.real = real
            self.imag = imag
            return self
        elif isinstance(other, str):
            return self * ComplexNumber(other)
        else:
            raise OwnError(f'{other} - incorrect type')

    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            real = (self.real * other.real + self.imag * other.imag) / (other.real ** 2 + other.imag ** 2)
            imag = (other.real * self.imag - self.real * other.imag) / (other.real ** 2 + other.imag ** 2)
            return ComplexNumber(f'{real if real != 0 else ""}{"+" if imag > 0 and real != 0 else ""}'
                                 f'{f"{imag}j" if imag != 0 else ""}')
        elif isinstance(other, str):
            return self / ComplexNumber(other)
        else:
            raise OwnError(f'{other} - incorrect type')

    def __itruediv__(self, other):
        if isinstance(other, ComplexNumber):
            real = (self.real * other.real + self.imag * other.imag) / (other.real ** 2 + other.imag ** 2)
            imag = (other.real * self.imag - self.real * other.imag) / (other.real ** 2 + other.imag ** 2)
            elf.real = real
            self.imag = imag
            return ComplexNumber(f'{real if real != 0 else ""}{"+" if imag > 0 and real != 0 else ""}'
                                 f'{f"{imag}j" if imag != 0 else ""}')
        elif isinstance(other, str):
            return self / ComplexNumber(other)
        else:
            raise OwnError(f'{other} - incorrect type')

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            real = self.real - other.real
            imag = self.imag - other.imag
            return ComplexNumber(f'{real if real != 0 else ""}{"+" if imag > 0 and real != 0 else ""}'
                                 f'{f"{imag}j" if imag != 0 else ""}')
        elif isinstance(other, str):
            return self - ComplexNumber(other)
        else:
            raise OwnError(f'{other} - incorrect type')

    def __isub__(self, other):
        if isinstance(other, ComplexNumber):
            self.real = self.real - other.real
            self.imag = self.imag - other.imag
            return self
        elif isinstance(other, str):
            return self - ComplexNumber(other)
        else:
            raise OwnError(f'{other} - incorrect type')

if __name__ == '__main__':
    example_1 = ComplexNumber(100)
    print(example_1)
    example_2 = ComplexNumber('34j')
    print(example_2)
    example_3 = ComplexNumber('-34-18j')
    print(example_3)
    example_4 = ComplexNumber('-34j+12')
    print(example_4)
    print(example_2 + example_3)
    print(example_2 + "100")
    example_2 += "200"
    print(example_2)
    print(example_3 * example_4)
    example_2 *= "-200+3j"
    print(example_2)
    print(example_3 / example_4)
    example_2 /= "-200+3j"
    print(example_2)
