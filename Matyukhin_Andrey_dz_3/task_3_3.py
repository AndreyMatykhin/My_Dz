def thesaurus(*args, sort=None):
    tres_dict = {}
    for name in args:  # Переберем аргументы, переданные на вход функции
        if name[0].upper() in tres_dict:  # Если ключ с первой буквой аргумента в словаре уже есть,
            tres_dict[name[0].upper()].append((name.lower().title()))  # то дополним список по ключу новым элементом
            if sort == "forward":  # Отсортируем элементы в списке, если это нужно
                tres_dict[name[0].upper()].sort()
            elif sort == "reverse":
                tres_dict[name[0].upper()].sort(reverse=True)
        else:
            tres_dict[name[0].upper()] = [(name.lower().title())]  # Если ключа с первой буквой аргумента в словаре нет,
            #  то создадим его
    return tres_dict  # Передадим полученый словарь на выход


sample_names = ["Иван", "Мария", "Петр", "Илья", "Павел"]
print(thesaurus(*sample_names))
print(thesaurus(*sample_names, sort="forward"))
print(thesaurus(*sample_names, sort="reverse"))
