from utils import currency_rates  # Подключаем функцию из модуля
import sys

print(', '.join(map(str,currency_rates(sys.argv[1])[1:])))
