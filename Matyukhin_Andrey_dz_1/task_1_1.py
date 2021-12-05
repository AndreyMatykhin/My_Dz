duration = 1
while duration:
    duration = int(input("Введите период в секундах или 0 для выхода: "))  # Запрашиваем период для обработки
    if duration // 86400:  # Проверяем длительность на превышение суток
        print(str(duration // 86400) + " дн " + str((duration // 3600) % 24) + " час " + str(
            (duration // 60) % 60) + " мин " + str(
            duration % 60) + " сек")  # Выводим результат в формате <d> дн <h> час <m> мин <s> сек.
    elif duration // 3600:  # Проверяем длительность на превышение часа
        print(str(duration // 3600) + " час " + str((duration // 60) % 60) + " мин " + str(
            duration % 60) + " сек")  # Выводим результат в формате  <h> час <m> мин <s> сек
    elif duration // 60:  # Проверяем длительность на превышение минуты
        print(
            str(duration // 60) + " мин " + str(duration % 60) + " сек")  # Выводим результат в формате <m> мин <s> сек
    elif duration:
        print(str(duration % 60) + " сек")  # Выводим результат в формате <s> сек
    else:
        print("Выход ")
