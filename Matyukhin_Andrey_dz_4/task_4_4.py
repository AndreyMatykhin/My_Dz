from utils import currency_rates  # Подключаем функцию из модуля

# Производим несколько вызовов
print('INR = ', currency_rates('INR')[0])
print('KRW = ', currency_rates('KRW')[0])
print('ZAR = ', currency_rates('ZAR')[0])
print('CAD = ', currency_rates('cad')[0:2])
print('EUr = ', currency_rates('EUr')[0])
print('USD = ', currency_rates('USD')[0])
print('EUR = ', currency_rates('EUR')[0])
print('ZZZ = ', currency_rates('ZZZ')[0])
print('JPY = ', currency_rates('JPY')[0])
