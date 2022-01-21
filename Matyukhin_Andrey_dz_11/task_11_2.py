class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    try:
        a = float(input("Введите делимое: "))
    except ValueError:
        raise OwnError("Введеное делимое не является дестичным числом")
    else:
        try:
            b = float(input("Введите делитель: "))
        except ValueError:
            raise OwnError("Введенный делитель не является дестичным числом")
        else:
            if b == 0:
                raise OwnError("Делить на ноль нельзя")
            else:
                res = a / b
except OwnError as err:
    print(err)
else:
    print(f'Полученый результат {str(a)} / {str(b)} = {str(res)}')
