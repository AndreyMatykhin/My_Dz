def num_translate(eng_word):
    trans_dict = {"one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять", "six": "шесть",
                  "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}  # Создадим словарь для
    # хранения значения переводов
    return trans_dict[eng_word] if eng_word in trans_dict else None  # используем тернанрный оператор для выбора
    # возвращаемого значения


print(num_translate("one"))
print(num_translate("eight"))
print(num_translate('tlw'))
