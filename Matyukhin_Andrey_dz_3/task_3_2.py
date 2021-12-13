def num_translate_adv(eng_word):
    trans_dict = {"one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять", "six": "шесть",
                  "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}  # Создадим словарь для
    # хранения значения переводов
    return trans_dict[eng_word] if eng_word in trans_dict else trans_dict[
        eng_word.lower()].title() if eng_word.istitle() and eng_word.lower() in trans_dict else None  # используем
    # тернанрный оператор для выбора возвращаемого значения


print(num_translate_adv("one"))
print(num_translate_adv("eight"))
print(num_translate_adv("One"))
print(num_translate_adv("two"))
print(num_translate_adv('tlw'))
