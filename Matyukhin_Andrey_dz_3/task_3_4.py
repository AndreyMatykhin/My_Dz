def thesaurus_adv(*args, sort=None):
    tres_dict = {}
    for name in args:  # Переберем аргументы, переданные на вход функции
        if name.split()[1][0].upper() in tres_dict:  # Если ключ с первой буквой фамилии в словаре уже есть,
            if name.split()[0][0].upper() in tres_dict[name.split()[1][0].upper()]:  # то проверить есть ли ключ по
                # первой букве имени и добавитиь в список новые данне, после чего отсортировать их (если нужно)
                tres_dict[name.split()[1][0].upper()][name.split()[0][0].upper()].append(name.lower().title())
                if sort == "forward":
                    tres_dict[name.split()[1][0].upper()][name.split()[0][0].upper()].sort(key=lambda x: x.split()[1])
                elif sort == "reverse":
                    tres_dict[name.split()[1][0].upper()][name.split()[0][0].upper()].sort(reverse=True,
                                                                                           key=lambda x: x.split()[1])
            else:  # Если ключа с первой буквой имени нет, то добавить его и начать список
                tres_dict[name.split()[1][0]][name.split()[0][0].upper()] = [(name.lower().title())]
        else:  # Если ключ с первой буквой фамилии в словаре нет, то добавить его и словарь с словарем по ключу по
            # первой букве имени и поле списка
            tres_dict[name.split()[1][0].upper()] = {name.split()[0][0].upper(): [(name.lower().title())]}
    return tres_dict  # Передадим полученый словарь на выход


sample_names = ["Иван Сергеев", "Анна Савельева", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Андрей Скуратов"]
print(thesaurus_adv(*sample_names))
print(thesaurus_adv(*sample_names, sort="forward"))
print(thesaurus_adv(*sample_names, sort="reverse"))
