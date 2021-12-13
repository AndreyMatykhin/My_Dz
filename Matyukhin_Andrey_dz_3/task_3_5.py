def get_jokes(n, repeat=False):
    """Please do not use "n" values greater than 5 for the condition "repeat" = false"""  # Документируем функцию,
    # прописав ограничения
    from random import sample, choice  # подключим функции из модуля Random
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    if repeat:  # Если можно повторять слова шуток, то сгенерируем список шуток, случайно выбирая слова из заданных
        # списков
        return [f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}" for k in range(n)]
    else:  # Если слова повторять нельза, то перемешаем исходные списки, склеем их в список шуток и случайно выберем
        # заданое количество шуток из получившегося списка
        return sample([f"{a} {b} {c}" for a, b, c, in zip(sample(nouns, len(nouns)), sample(adverbs, len(adverbs)),
                                                          sample(adjectives, len(adjectives)))], n)


print(get_jokes(7, repeat=True))
print(get_jokes(3))
