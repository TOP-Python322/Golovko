# ИСПРАВИТЬ: данная функция не возвращает None
def countable_nouns(num: int, nouns: tuple[str, str, str]) -> str | None:
    """Returns the noun of Russian language compatible with number."""
    # ПЕРЕИМЕНОВАТЬ: плохая идея использовать здесь _
    # ИСПРАВИТЬ: с работой функции round() в данном случае прекрасно справится оператор целочисленного деления //
    _ = round((num % 100) / 10)
    if _ != 1 and num % 10 == 1:
        return nouns[0]
    elif _ != 1 and num % 10 in [2, 3, 4]:
        return nouns[1]
    else:
        return nouns[2]


# >>> countable_nouns(1, ("год", "года", "лет"))
# 'год'
# >>> countable_nouns(2, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(10, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(12, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(22, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(11, ("год", "года", "лет"))
# 'лет'


# ИТОГ: хорошо, немного доработать — 4/6
