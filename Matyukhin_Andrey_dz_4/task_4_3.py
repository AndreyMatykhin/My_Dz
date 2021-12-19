# Подключаем модули
from requests import get
from decimal import Decimal
from datetime import datetime


def currency_rates(val):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')  # запрашиваем сайт Центрбанка
    content = response.content.decode(encoding="windows-1251")  # Перекодируем полученюу страницу
    val_curs = {}  # Создаем словарь для хранения джанных о курсах валют
    today_date = datetime.strptime(content.split("<Valute ")[0].split('"')[5], "%d.%m.%Y")  # Сохраним дату
    for el in content.split("<Valute ")[1:]:  # Заполняем слварь данными из страницы
        val_curs[el.split("><")[2][9:12]] = {"Name": el.split("><")[4][5:(len(el.split("><")[4]) - 6)],
                                             "ID": el.split("><")[0][4:(len(el.split("><")[0]) - 1)],
                                             "NumCode": el.split("><")[1][8:11],
                                             "Nominal": int(el.split("><")[3][8:(len(el.split("><")[3]) - 9)]),
                                             "Value": Decimal(
                                                 el.split("><")[5].replace(",", ".")[6:(len(el.split("><")[5]) - 7)])}
    return (f'На {today_date.strftime("%Y-%m-%d")} "{val.upper()}" равен '
            f'{val_curs[val.upper()]["Value"].quantize(Decimal("1.00"))}'
            f' руб. за {val_curs[val.upper()]["Nominal"]} {val_curs[val.upper()]["Name"]}',
            val_curs[val.upper()]["Value"].quantize(Decimal("1.00")),
            today_date.strftime("%Y-%m-%d")) if val.upper() in val_curs else [None, None, None]
    # Формируем ответ


if __name__ == '__main__':
    print('USD = ', currency_rates('USD')[0])
    print('EUR = ', currency_rates('EUR')[0])
    print('JPY = ', currency_rates('JPY')[0])
    print('KRW = ', currency_rates('KRW')[0])
    print('ZAR = ', currency_rates('ZAR')[0])
    print('ZZZ = ', currency_rates('ZZZ')[0])
    print('UsD = ', currency_rates('UsD')[0])
    print('EUr = ', currency_rates('EUr')[0])
    print('JPY = ', currency_rates('JPY')[0])
