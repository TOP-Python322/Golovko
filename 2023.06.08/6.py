from math import sqrt


def orth_triangle(
        # ИСПРАВИТЬ: согласно условию, аргументы должны быть строго ключевыми
        cathet1: float = 0,
        cathet2: float = 0,
        hypotenuse: float = 0
) -> float | None:
    """Calculate third side of rectangular triangle on two others sides."""
    # ИСПРАВИТЬ: проверок недостаточно (см. примеры ниже)
    # СДЕЛАТЬ: подумайте, как можно лучше сформулировать эти проверки
    if (
            hypotenuse != 0
        and (hypotenuse < cathet1 or hypotenuse < cathet2)
         or (hypotenuse != 0 and cathet1 != 0 and cathet2 != 0)
    ):
        return None
    else:
        if hypotenuse == 0:
            # ИСПОЛЬЗОВАТЬ: не множьте сущности в коде
            return sqrt(cathet1 * cathet1 + cathet2 * cathet2)
        elif cathet1 == 0:
            # cathet1 = sqrt(hypotenuse * hypotenuse - cathet2 * cathet2)
            # ИСПОЛЬЗОВАТЬ: прямо просится оператор **
            cathet1 = (hypotenuse ** 2 - cathet2 ** 2) ** 0.5
            return cathet1
        elif cathet2 == 0:
            cathet2 = sqrt(hypotenuse*hypotenuse - cathet1*cathet1)
            return cathet2
        

# >>> orth_triangle(cathet1=3, hypotenuse=5)
# 4.0
# >>> orth_triangle(cathet1=8, cathet2=15)
# 17.0
# >>> orth_triangle(cathet2=9, hypotenuse=3)
# None

# >>> print(orth_triangle())
# КОММЕНТАРИЙ: а должно быть None
# 0.0

# КОММЕНТАРИЙ: некорректная передача аргумента
# >>> print(orth_triangle(1))
# КОММЕНТАРИЙ: даже при передаче по ключу, но только одного аргумента, должно быть None
# 1.0


# ИТОГ: нужно лучше, доработать — 2/5
