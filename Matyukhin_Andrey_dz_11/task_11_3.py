class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


numb_list = []
numb = ''
while numb != "stop":
    numb = input('Введите число для добавления в список или\n слово "stop" '
                 'для остановки процесса формирования списка и вывода сформированного списка:')
    if numb != "stop":
        try:
            try:
                numb = int(numb)
            except ValueError:
                try:
                    numb = float(numb)
                except ValueError:
                    raise OwnError(f'Введенное значение "{numb}" не является числом. Попробуйте еще раз.')
        except OwnError as err:
            print(err)
        else:
            numb_list.append(numb)
else:
    print(f'Поздравляем!'.center(50, "-"))
    print(f'Вы сформировали список из чисел: {", ".join([str(x) for x in numb_list])}'.center(50, " "))
